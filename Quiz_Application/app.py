from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key-123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quiz.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Database Models
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    scores = db.relationship('Score', backref='user', lazy=True)

class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    questions = db.relationship('Question', backref='quiz', lazy=True)

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    choices = db.relationship('Choice', backref='question', lazy=True)

class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    quiz = db.relationship('Quiz')

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        if current_user.is_admin:
            return redirect(url_for('admin'))
        return redirect(url_for('quizzes'))
    return redirect(url_for('login'))

@app.route('/login')
def login():
    """Landing page - asks user to choose Admin or Student"""
    return render_template('login.html')

@app.route('/admin_login', methods=['GET', 'POST'])
def admin_login():
    """Admin login page"""
    if current_user.is_authenticated and current_user.is_admin:
        return redirect(url_for('admin'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username, is_admin=True).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('admin'))
        flash('Invalid admin credentials', 'error')
    return render_template('admin_login.html')

@app.route('/student_login', methods=['GET', 'POST'])
def student_login():
    """Student login page"""
    if current_user.is_authenticated and not current_user.is_admin:
        return redirect(url_for('quizzes'))
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password_hash, password):
            login_user(user)
            return redirect(url_for('quizzes'))
        flash('Invalid username or password', 'error')
    return render_template('login.html', login_mode=True)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        
        if User.query.filter_by(username=username).first():
            flash('Username already exists', 'error')
            return redirect(url_for('register'))
        
        hashed_password = generate_password_hash(password)
        new_user = User(username=username, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        flash('Registration successful! Please login.', 'success')
        return redirect(url_for('student_login'))
    return render_template('register.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/quizzes')
@login_required
def quizzes():
    all_quizzes = Quiz.query.all()
    return render_template('index.html', quizzes=all_quizzes)

@app.route('/quiz/<int:quiz_id>')
@login_required
def quiz(quiz_id):
    quiz_obj = Quiz.query.get_or_404(quiz_id)
    # Check if user already took this quiz
    existing_score = Score.query.filter_by(user_id=current_user.id, quiz_id=quiz_id).first()
    return render_template('quiz.html', quiz=quiz_obj, existing_score=existing_score)

@app.route('/result/<int:score_id>')
@login_required
def result(score_id):
    score = Score.query.get_or_404(score_id)
    if score.user_id != current_user.id:
        return redirect(url_for('quizzes'))
    quiz_obj = Quiz.query.get(score.quiz_id)
    return render_template('result.html', score=score, quiz=quiz_obj)

@app.route('/leaderboard')
@login_required
def leaderboard():
    scores = Score.query.order_by(Score.score.desc()).limit(20).all()
    return render_template('leaderboard.html', scores=scores)

# Admin routes
@app.route('/admin')
@login_required
def admin():
    if not current_user.is_admin:
        flash('Access denied', 'error')
        return redirect(url_for('quizzes'))
    quizzes = Quiz.query.all()
    users = User.query.filter_by(is_admin=False).all()
    return render_template('admin.html', quizzes=quizzes, users=users)

@app.route('/admin/create-quiz', methods=['POST'])
@login_required
def create_quiz():
    if not current_user.is_admin:
        return jsonify({'error': 'Access denied'}), 403
    
    title = request.form.get('title')
    description = request.form.get('description')
    
    new_quiz = Quiz(title=title, description=description)
    db.session.add(new_quiz)
    db.session.commit()
    
    flash('Quiz created successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/add-question', methods=['POST'])
@login_required
def add_question():
    if not current_user.is_admin:
        return jsonify({'error': 'Access denied'}), 403
    
    quiz_id = request.form.get('quiz_id')
    question_text = request.form.get('question_text')
    choices = request.form.getlist('choices[]')
    correct_choice = int(request.form.get('correct_choice'))
    
    new_question = Question(quiz_id=quiz_id, question_text=question_text)
    db.session.add(new_question)
    db.session.commit()
    
    for i, choice_text in enumerate(choices):
        is_correct = (i == correct_choice)
        choice = Choice(question_id=new_question.id, choice_text=choice_text, is_correct=is_correct)
        db.session.add(choice)
    
    db.session.commit()
    flash('Question added successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/add_student', methods=['POST'])
@login_required
def add_student():
    """Add a new student (admin only)"""
    if not current_user.is_admin:
        flash('Access denied', 'error')
        return redirect(url_for('quizzes'))
    
    username = request.form.get('username')
    password = request.form.get('password')
    
    if User.query.filter_by(username=username).first():
        flash('Username already exists', 'error')
        return redirect(url_for('admin'))
    
    hashed_password = generate_password_hash(password)
    new_student = User(username=username, password_hash=hashed_password, is_admin=False)
    db.session.add(new_student)
    db.session.commit()
    
    flash('Student added successfully!', 'success')
    return redirect(url_for('admin'))

@app.route('/admin/delete_student/<int:user_id>', methods=['POST'])
@login_required
def delete_student(user_id):
    """Delete a student (admin only)"""
    if not current_user.is_admin:
        flash('Access denied', 'error')
        return redirect(url_for('quizzes'))
    
    user = User.query.get_or_404(user_id)
    
    # Don't allow deleting admin users
    if user.is_admin:
        flash('Cannot delete admin users', 'error')
        return redirect(url_for('admin'))
    
    # Delete user's scores first
    Score.query.filter_by(user_id=user_id).delete()
    db.session.delete(user)
    db.session.commit()
    
    flash('Student deleted successfully!', 'success')
    return redirect(url_for('admin'))

# API Routes
@app.route('/api/quiz/<int:quiz_id>')
@login_required
def get_quiz(quiz_id):
    quiz_obj = Quiz.query.get_or_404(quiz_id)
    questions = []
    for q in quiz_obj.questions:
        choices = [{'id': c.id, 'text': c.choice_text} for c in q.choices]
        questions.append({
            'id': q.id,
            'text': q.question_text,
            'choices': choices
        })
    return jsonify({
        'id': quiz_obj.id,
        'title': quiz_obj.title,
        'description': quiz_obj.description,
        'questions': questions
    })

@app.route('/api/submit', methods=['POST'])
@login_required
def submit_quiz():
    data = request.json
    quiz_id = data.get('quiz_id')
    answers = data.get('answers', {})
    
    quiz_obj = Quiz.query.get_or_404(quiz_id)
    score = 0
    total = len(quiz_obj.questions)
    
    for question in quiz_obj.questions:
        selected_choice_id = answers.get(str(question.id))
        if selected_choice_id:
            choice = Choice.query.get(selected_choice_id)
            if choice and choice.is_correct:
                score += 1
    
    # Save score
    new_score = Score(user_id=current_user.id, quiz_id=quiz_id, score=score, total_questions=total)
    db.session.add(new_score)
    db.session.commit()
    
    return jsonify({
        'score_id': new_score.id,
        'score': score,
        'total': total
    })

@app.route('/api/scores')
@login_required
def get_scores():
    scores = Score.query.filter_by(user_id=current_user.id).order_by(Score.completed_at.desc()).all()
    return jsonify([{
        'id': s.id,
        'quiz_title': s.quiz.title,
        'score': s.score,
        'total': s.total_questions,
        'date': s.completed_at.strftime('%Y-%m-%d %H:%M')
    } for s in scores])

# Create database and sample data
def init_db():
    with app.app_context():
        db.create_all()
        
        # Create admin user if not exists
        if not User.query.filter_by(username='admin').first():
            admin = User(
                username='admin',
                password_hash=generate_password_hash('admin123'),
                is_admin=True
            )
            db.session.add(admin)
        
        # Create sample quiz if no quizzes exist
        if not Quiz.query.first():
            sample_quiz = Quiz(
                title='Python Basics',
                description='Test your Python knowledge!'
            )
            db.session.add(sample_quiz)
            db.session.commit()
            
            # Add sample questions
            q1 = Question(quiz_id=sample_quiz.id, question_text='What is the output of print(2+3)?')
            db.session.add(q1)
            db.session.commit()
            
            choices_q1 = [
                Choice(question_id=q1.id, choice_text='5', is_correct=True),
                Choice(question_id=q1.id, choice_text='23', is_correct=False),
                Choice(question_id=q1.id, choice_text='Error', is_correct=False),
            ]
            for c in choices_q1:
                db.session.add(c)
            
            q2 = Question(quiz_id=sample_quiz.id, question_text='Which keyword is used to define a function in Python?')
            db.session.add(q2)
            db.session.commit()
            
            choices_q2 = [
                Choice(question_id=q2.id, choice_text='function', is_correct=False),
                Choice(question_id=q2.id, choice_text='def', is_correct=True),
                Choice(question_id=q2.id, choice_text='func', is_correct=False),
            ]
            for c in choices_q2:
                db.session.add(c)
            
            q3 = Question(quiz_id=sample_quiz.id, question_text='What is the correct way to create a list in Python?')
            db.session.add(q3)
            db.session.commit()
            
            choices_q3 = [
                Choice(question_id=q3.id, choice_text='list()', is_correct=False),
                Choice(question_id=q3.id, choice_text='[1, 2, 3]', is_correct=True),
                Choice(question_id=q3.id, choice_text='{1, 2, 3}', is_correct=False),
            ]
            for c in choices_q3:
                db.session.add(c)
            
            db.session.commit()
        
        print("Database initialized successfully!")

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
