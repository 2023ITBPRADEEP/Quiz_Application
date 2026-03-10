# ABSTRACT

**QUIZ APPLICATION** is a platform that helps students and learners with online assessment and evaluation. **QUIZ APPLICATION** is an online quiz system that connects educators with students, bridging the gap between teaching and learning. It's a platform that enables students to access quizzes and tests they need, when they need them, without the limitations of traditional paper-based testing. The quiz process and improve modern educational methods.

In such a way we are introducing a website which is dynamic with capable of multitasking features, it is named as "Quiz Application", Here we use this website for student benefit. This project aims to promote the sharing economy within the educational sector, enabling cost effective solution for students.

This website is developed with Python, Flask and SQLite.

---

# CHAPTER 1 : INTRODUCTION

## 1.1 An Overview of the Project

Internet today is performing tremendous changes in all fields. They are fast changing the way in which work is done by their speed, accuracy and diligence. Almost all good business practices have embraced websites for increasing the productivity and efficiency, which ultimately results in goodwill. Each and every business people hosting their own website which may be of static or dynamic according to the business nature.

In such a way we introducing a website which is dynamic with capable of multitasking features, it is named as "Quiz Application", Here we use this website for student benefit. This project aims to promote the sharing economy within the educational sector, enabling cost effective solution for students.

This website is developed with Python, Flask and SQLite.

## 1.2 Module Description

### ADMIN MODULE

**Dashboard:** A comprehensive overview of available quizzes, registered users, and system activities.

**Quiz Management:** The ability to create, update, or delete quizzes with title and description.

**Question Management:** Add, edit, or remove questions with multiple choice options for each quiz.

**Student Management:** View and manage details of all registered students on the platform.

**Quiz Statistics:** View quiz completion statistics, scores, and performance metrics.

**Leaderboard Management:** Monitor and track student rankings based on quiz performance.

### USER MODULE

**1. Guest Users:** Can explore the platform, view available quizzes, and register for more features.

**2. Registered Users:** Have full access to quiz taking, results, and personalized services. Features include:

- **My Quizzes:** Browse available quizzes, take quizzes, and view quiz history.
- **My Results:** Track quiz scores, view performance, and analyze progress.
- **Leaderboard:** View rankings and compare scores with other students.
- **My Account:** Update profile information, manage passwords, and ensure account security.

## 1.3 Aim of the Work
The aim of this work is to develop a user-friendly, efficient, and reliable online platform for conducting quizzes and evaluating student performance. The platform will:
- Empower students: Access to a wider range of quizzes without geographical limitations, allowing them to test their knowledge and improve their learning outcomes.
- Benefit educators: Provide a platform for teachers to create and manage quizzes, track student progress, and analyze performance metrics.
- Promote accessibility: Reduce the need for physical examination halls, making assessments more accessible to students anywhere.
- Enhance efficiency: Streamline the assessment process with automated scoring, instant feedback, and result analysis.
- Increase transparency: By creating a central platform for assessments, students can easily track their progress and compare performance.
- Promote innovation: The platform could encourage educators to develop more engaging quiz content, leading to advancements in educational technology.
- Support learning communities: By connecting students and educators within the same platform, the system can strengthen educational communities.

---

# CHAPTER 2 : BACKGROUND STUDY

## 2.1 A Study of the Existing System
Traditional quiz systems often lack real-time interaction, automated scoring, and competitive features. Existing manual quiz systems require teachers to manually evaluate answers and maintain records, which is time-consuming and prone to errors. There is a need for an automated, web-based quiz system that can:
- Provide instant feedback and scoring
- Track user performance over time
- Enable competitive learning through leaderboards
- Allow easy quiz creation and management

---

# CHAPTER 3 : SYSTEM ANALYSIS

## 3.1 A Study on the Proposed System

### 3.1.1 ADVANTAGES OF PROPOSED SYSTEM

1. **User-Friendly Interface**: Intuitive design with separate login pages for admin and students
2. **Real-Time Quiz Taking**: Dynamic quiz loading with countdown timer
3. **Automated Scoring**: Instant score calculation upon quiz submission
4. **Role-Based Access Control**: Separate dashboards for administrators and students
5. **Persistent Storage**: SQLite database for reliable data management
6. **Security**: Password hashing using Werkzeug security features
7. **Responsive Design**: Clean CSS styling for better user experience

### Users of the System:
1. **Administrator**
   - Create and manage quizzes
   - Add questions with multiple choice options
   - Manage students (add/delete)
   - View all quizzes and users

2. **Student**
   - Register and login
   - View available quizzes
   - Take quizzes within time limit
   - View results and scores
   - View leaderboard

## 3.2 Definition of the Problem
The current project addresses the need for a comprehensive online quiz management system that can:
- Allow administrators to easily create and manage quizzes
- Enable students to take quizzes online with automatic scoring
- Provide a competitive environment through leaderboard tracking
- Maintain secure user authentication and authorization

## 3.3 Developing Solution Strategies
The solution is developed using:
- **Flask** as the web framework for rapid development
- **SQLAlchemy** for database operations and ORM
- **Flask-Login** for user authentication management
- **HTML/CSS/JavaScript** for responsive frontend
- **SQLite** for lightweight, embedded database storage

## 3.4 System Specification

### 3.4.1 Hardware Requirements
- **Processor**: Any modern processor (Intel Core i3 or equivalent)
- **RAM**: Minimum 4GB
- **Storage**: 100MB for application files
- **Display**: Standard monitor with 1024x768 resolution

### 3.4.2 Software Specification
- **Languages**: PHP, HTML
- **Database**: MySQL
- **Operating System**: Any type of OS
- **Web Server**: Apache, Wamp
- **Portable Devices**: WAMPP
- **Network Port**: 100 Mbps

### 3.4.3 Frontend Tools
- **HTML5**: Markup language for web pages
- **CSS3**: Styling and responsive design
- **JavaScript (ES6+)**: Client-side scripting for dynamic functionality

### 3.4.4 Backend Tools
- **Flask 3.0.0**: Lightweight WSGI web application framework
- **Flask-SQLAlchemy 3.1.1**: ORM for database operations
- **Flask-Login 0.6.3**: User authentication management
- **Werkzeug 3.0.1**: Password hashing and security utilities

### 3.5 Final Outline Proposed System
The Quiz Application will provide a complete solution for online quiz management with separate portals for administrators and students. The system will feature secure authentication, automated scoring, and competitive leaderboards.

---

# CHAPTER 4 : SYSTEM STUDY AND DESIGN

## 4.1 UML Diagram

### Class Diagram

### Database Models:

| Model | Attributes |
|-------|------------|
| **User** | id, username, password_hash, is_admin, scores |
| **Quiz** | id, title, description, questions |
| **Question** | id, quiz_id, question_text, choices |
| **Choice** | id, question_id, choice_text, is_correct |
| **Score** | id, user_id, quiz_id, score, total_questions, completed_at |

## 4.2 Use Case Diagram

### Visual Use Case Diagram:

```
                    +---------------------------------------------------------+
                    |                    QUIZ APPLICATION                     |
                    |                                                          |
+-----------+       |     +---------------------------------------------+     |
|  STUDENT  |       |     |                                             |     |
|           |       |     |     +------------+                          |     |
|  -------- |       |     |     |  REGISTER  |<-----------------------+ |     |
|  * Register|      |     |     +------------+                          |     |
|  * Login   |------+-----+     |            |                           |     |
|  * View    |      |     |     +------------+                          |     |
|    Quizzes |      |     |     |    LOGIN    |<-------------------------+ |     |
|  * Take    |      |     |     +------------+                          |     |
|    Quiz    |      |     |     |            |                           |     |
|  * Submit  |      |     |     +------------+                          |     |
|    Quiz    |      |     |     | VIEW QUIZZES|<-----------------------+ |     |
|  * View    |      |     |     +------------+                          |     |
|    Results |      |     |     |            |                           |     |
|  * View    |      |     |     +------------+                          |     |
|    Leader- |      |     |     |  TAKE QUIZ  |<-----------------------+ |     |
|    board   |      |     |     +------------+                          |     |
+-----------+      |     |            |                                 |     |
                   |     |     +------------+                          |     |
+-----------+      |     |     |   SUBMIT    |<------------------------+ |     |
|  ADMINIS- |      |     |     |    QUIZ     |                         |     |
|  TRATOR   |      |     |     +------------+                          |     |
|           |      |     |            |                                 |     |
|  -------- |      |     |     +------------+                          |     |
|  * Login   |------+-----+     |  VIEW RESULT|<------------------------+ |     |
|  * Create  |      |     |     +------------+                          |     |
|    Quiz    |      |     |            |                                 |     |
|  * Add     |      |     |     +------------+                          |     |
|    Question|      |     |     |   VIEW       |<-----------------------+ |     |
|  * Manage  |      |     |     | LEADERBOARD  |                         |     |
|    Students|      |     |     +------------+                          |     |
|  * View    |      |     |                                             |     |
|    Dashboard|     |     |     +------------+                          |     |
+-----------+      |     |     |   CREATE     |                          |     |
                   |     |     |    QUIZ       |-------------------------+ |     |
                   |     |     +------------+                          |     |
                   |     |            |                                 |     |
                   |     |     +------------+                          |     |
                   |     |     |    ADD       |                          |     |
                   |     |     |  QUESTION    |-------------------------+ |     |
                   |     |     +------------+                          |     |
                   |     |            |                                 |     |
                   |     |     +------------+                          |     |
                   |     |     |    MANAGE    |                          |     |
                   |     |     |   STUDENTS   |-------------------------+ |     |
                   |     |     +------------+                          |     |
                   |     |            |                                 |     |
                   |     |     +------------+                          |     |
                   |     |     |     VIEW     |                          |     |
                   |     |     |   DASHBOARD  |-------------------------+ |     |
                   |     |     +------------+                          |     |
                   |     |                                             |     |
                   |     +---------------------------------------------+     |
                   |                                                          |
                   +----------------------------------------------------------+

Legend:
------->  : Direct Interaction (Primary Actor)
<-------  : System Response/Feedback
```

### Actors:
1. **Student** - Can register, login, take quizzes, view results, view leaderboard
2. **Administrator** - Can create quizzes, add questions, manage students, view dashboard

### Use Cases:
- **User Registration** - New students can create an account
- **User Login (Student/Admin)** - Authenticate users and administrators
- **View Available Quizzes** - Browse list of available quizzes
- **Take Quiz** - Answer questions within time limit
- **Submit Quiz & Calculate Score** - Submit answers and get automated scoring
- **View Results** - View quiz scores and performance
- **View Leaderboard** - View rankings and compare scores
- **Create Quiz (Admin)** - Create new quizzes with title and description
- **Add Question (Admin)** - Add questions with multiple choice options
- **Manage Students (Admin)** - View and delete student accounts
- **View Dashboard (Admin)** - Access admin dashboard with statistics

## 4.3 Data Flow Diagram

### Level 0 (Context Diagram):
```
┌─────────────────────────────────────────┐
│         Quiz Application                │
│                                         │
│  ┌──────────┐    ┌──────────┐          │
│  │ Student  │    │  Admin   │          │
│  └────┬─────┘    └────┬─────┘          │
│       │               │                │
│       └───────┬───────┘                │
│               ▼                        │
│         ┌─────┴─────┐                  │
│         │  System  │                   │
│         └──────────┘                   │
└─────────────────────────────────────────┘
```

### Level 1:
- **Authentication Module**: Handles login, registration, logout
- **Quiz Management Module**: Create quizzes, add questions
- **Quiz Taking Module**: Display questions, collect answers, calculate scores
- **Reporting Module**: Display results, leaderboard

## 4.4 ER Diagram

```
┌─────────────┐       ┌─────────────┐       ┌─────────────┐
│    User     │       │    Quiz     │       │  Question   │
├─────────────┤       ├─────────────┤       ├─────────────┤
│ id (PK)     │──1:N──│ id (PK)     │──1:N──│ id (PK)     │
│ username    │       │ title       │       │ quiz_id (FK)│
│ password_hash│      │ description │       │ question_text│
│ is_admin    │       └─────────────┘       └──────┬──────┘
└──────┬──────┘                                      │
       │                                             │
      1│N                                           1│N
       │                                             │
       ▼                                             ▼
┌─────────────┐                           ┌─────────────┐
│    Score    │                           │   Choice    │
├─────────────┤                           ├─────────────┤
│ id (PK)     │                           │ id (PK)     │
│ user_id (FK)│                           │ question_id │
│ quiz_id (FK)│                           │ choice_text │
│ score       │                           │ is_correct  │
│ total_questions│                         └─────────────┘
│ completed_at│
└─────────────┘
```

## 4.5 Design Process

### 4.5.1 Database Design

### Users Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| username | String(150) | Unique, Not Null |
| password_hash | String(200) | Not Null |
| is_admin | Boolean | Default: False |

### Quizzes Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| title | String(200) | Not Null |
| description | Text | Nullable |

### Questions Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| quiz_id | Integer | Foreign Key |
| question_text | Text | Not Null |

### Choices Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| question_id | Integer | Foreign Key |
| choice_text | Text | Not Null |
| is_correct | Boolean | Default: False |

### Scores Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| user_id | Integer | Foreign Key |
| quiz_id | Integer | Foreign Key |
| score | Integer | Not Null |
| total_questions | Integer | Not Null |
| completed_at | DateTime | Default: Current Time |

### 4.5.2 Input Design

### Forms:
1. **Login Form**: Username, Password
2. **Registration Form**: Username, Password
3. **Create Quiz Form**: Title, Description
4. **Add Question Form**: Question Text, 2-4 Choices, Correct Answer Selection
5. **Add Student Form**: Username, Password

### 4.5.3 Output Design

### Pages:
1. **Login Page**: Role selection (Admin/Student)
2. **Dashboard**: Available quizzes list
3. **Quiz Page**: Questions with multiple choice options, timer
4. **Result Page**: Score display with correct/incorrect summary
5. **Leaderboard**: Top 20 scores with username and points
6. **Admin Dashboard**: Quiz creation, student management

---

# CHAPTER 5 : TESTING AND IMPLEMENTATION

## 5.1 Testing

### 5.1.1 Testing Methodologies

1. **Unit Testing**: Individual component testing
2. **Integration Testing**: Testing module interactions
3. **User Acceptance Testing**: End-to-end workflow validation

## 5.2 Test Cases

| Test ID | Description | Expected Result |
|---------|-------------|-----------------|
| TC001 | User Registration | New user created in database |
| TC002 | Admin Login | Redirect to admin dashboard |
| TC003 | Student Login | Redirect to quiz list |
| TC004 | Create Quiz | Quiz added to database |
| TC005 | Add Question | Question linked to quiz |
| TC006 | Take Quiz | Questions displayed with timer |
| TC007 | Submit Quiz | Score calculated and saved |
| TC008 | View Leaderboard | Top scores displayed |
| TC009 | Delete Student | Student removed from database |
| TC010 | Quiz Timer Expiry | Quiz auto-submitted |

## 5.3 Testing Methodologies

### 5.3.1 Generic Risks

1. **Data Loss**: Database corruption prevention through regular backups
2. **Session Timeout**: Automatic logout after inactivity
3. **Input Validation**: Server-side validation for all inputs

### 5.3.2 Security Technologies and Policies

1. **Password Hashing**: Using Werkzeug's generate_password_hash
2. **Session Management**: Flask-Login for secure session handling
3. **Access Control**: Role-based route protection
4. **SQL Injection Prevention**: SQLAlchemy ORM prevents SQL injection

## 5.4 Quality Assurance

The system ensures quality through:
- Comprehensive input validation
- Secure password storage
- Role-based access control
- Error handling and logging
- Regular database backups

## 5.5 System Implementation

### 5.5.1 Implementation Procedure

1. Install Python dependencies: `pip install -r requirements.txt`
2. Run the application: `python app.py`
3. Access via browser: `http://localhost:5000`
4. Default admin credentials: username: `admin`, password: `admin123`

### 5.5.2 User Manual

**Starting the Application:**
```
python app.py
```

**Default Configuration:**
- Secret Key: your-secret-key-123
- Database: SQLite (quiz.db)
- Admin Username: admin
- Admin Password: admin123

**How to Use:**

1. **For Administrators:**
   - Login with admin credentials
   - Create new quizzes with title and description
   - Add questions with multiple choice options
   - Mark correct answers
   - Manage students (add/delete)
   - View all quizzes and users

2. **For Students:**
   - Register a new account
   - Login with student credentials
   - View available quizzes
   - Start a quiz and answer questions
   - View results after submission
   - Check leaderboard for rankings

## 5.6 System Maintenance

### Maintenance Activities:
1. **Database Backup**: Regular export of quiz.db
2. **Log Monitoring**: Review application logs for errors
3. **User Management**: Periodic review of user accounts
4. **Quiz Updates**: Add new quizzes and questions as needed

---

# CHAPTER 6 : CONCLUSION

## 6.1 Future Enhancement

Future enhancements for the Quiz Application may include:

1. **Multiple Choice Question Types**: Add true/false, fill-in-the-blank questions
2. **Quiz Categories**: Organize quizzes by subject/topic
3. **Time Limits Per Question**: Individual timers for each question
4. **Analytics Dashboard**: Detailed performance analytics for admins
5. **Email Notifications**: Send results via email
6. **REST API**: Mobile app support
7. **Social Features**: Share scores on social media
8. **Multi-language Support**: Localization for different languages
9. **Certificate Generation**: Award certificates for passing quizzes
10. **Real-time Competition**: Live quiz sessions with multiple players

---

# Annexure-A – Table Design

## Database Schema

### Users Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| username | String(150) | Unique, Not Null |
| password_hash | String(200) | Not Null |
| is_admin | Boolean | Default: False |

### Quizzes Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| title | String(200) | Not Null |
| description | Text | Nullable |

### Questions Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| quiz_id | Integer | Foreign Key |
| question_text | Text | Not Null |

### Choices Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| question_id | Integer | Foreign Key |
| choice_text | Text | Not Null |
| is_correct | Boolean | Default: False |

### Scores Table
| Field | Type | Constraints |
|-------|------|-------------|
| id | Integer | Primary Key |
| user_id | Integer | Foreign Key |
| quiz_id | Integer | Foreign Key |
| score | Integer | Not Null |
| total_questions | Integer | Not Null |
| completed_at | DateTime | Default: Current Time |

---

# Annexure-B – Screen Shots & Reports

## Screen 1: Login Page
- Title: "Quiz Application"
- Options: "Admin Login" and "Student Login"
- Registration link for new students

## Screen 2: Admin Dashboard
- Quiz creation form
- Student management table
- Quiz listing with question counts
- Add question modal

## Screen 3: Quiz List (Student)
- Grid of available quizzes
- Quiz title, description, question count
- "Start Quiz" button for each quiz

## Screen 4: Quiz Taking Page
- Quiz title header
- Countdown timer (10 minutes)
- Question cards with radio button options
- Submit button

## Screen 5: Result Page
- Score display (X/Y correct)
- Percentage score
- "Back to Quizzes" and "View Leaderboard" buttons

## Screen 6: Leaderboard
- Top 20 scores table
- Columns: Rank, Username, Score, Quiz, Date

---

# Annexure-C – Sample Source Code

## Database Models (app.py)

```
python
# User Model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    scores = db.relationship('Score', backref='user', lazy=True)

# Quiz Model
class Quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    questions = db.relationship('Question', backref='quiz', lazy=True)

# Question Model
class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    question_text = db.Column(db.Text, nullable=False)
    choices = db.relationship('Choice', backref='question', lazy=True)

# Choice Model
class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'), nullable=False)
    choice_text = db.Column(db.Text, nullable=False)
    is_correct = db.Column(db.Boolean, default=False)

# Score Model
class Score(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    total_questions = db.Column(db.Integer, nullable=False)
    completed_at = db.Column(db.DateTime, default=datetime.utcnow)
    quiz = db.relationship('Quiz')
```

## Quiz Submission API (app.py)

```
python
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
```

## Timer Function (templates/quiz.html)

```
javascript
function startTimer() {
    timerInterval = setInterval(() => {
        timeRemaining--;
        const minutes = Math.floor(timeRemaining / 60);
        const seconds = timeRemaining % 60;
        document.getElementById('timer').textContent = 
            `${minutes}:${seconds.toString().padStart(2, '0')}`;
        
        if (timeRemaining <= 0) {
            clearInterval(timerInterval);
            submitQuiz();
        }
    }, 1000);
}
```

---

*Document prepared for Quiz Application Project*
*Technology Stack: Python, Flask, SQLite, HTML, CSS, JavaScript*
