/**
 * Quiz Application JavaScript
 */

// API Utility Functions
const API = {
    async getQuiz(quizId) {
        const response = await fetch(`/api/quiz/${quizId}`);
        if (!response.ok) {
            throw new Error('Failed to fetch quiz');
        }
        return response.json();
    },

    async submitQuiz(quizId, answers) {
        const response = await fetch('/api/submit', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                quiz_id: quizId,
                answers: answers
            })
        });
        if (!response.ok) {
            throw new Error('Failed to submit quiz');
        }
        return response.json();
    },

    async getScores() {
        const response = await fetch('/api/scores');
        if (!response.ok) {
            throw new Error('Failed to fetch scores');
        }
        return response.json();
    }
};

// Quiz Timer
class QuizTimer {
    constructor(duration, onTimeUp) {
        this.duration = duration;
        this.onTimeUp = onTimeUp;
        this.timeRemaining = duration;
        this.interval = null;
    }

    start() {
        this.interval = setInterval(() => {
            this.timeRemaining--;
            this.updateDisplay();

            if (this.timeRemaining <= 0) {
                this.stop();
                if (this.onTimeUp) {
                    this.onTimeUp();
                }
            }
        }, 1000);
    }

    stop() {
        if (this.interval) {
            clearInterval(this.interval);
            this.interval = null;
        }
    }

    updateDisplay() {
        const timerElement = document.getElementById('timer');
        if (timerElement) {
            const minutes = Math.floor(this.timeRemaining / 60);
            const seconds = this.timeRemaining % 60;
            timerElement.textContent = `${minutes}:${seconds.toString().padStart(2, '0')}`;

            // Change color when time is running low
            if (this.timeRemaining <= 60) {
                timerElement.style.color = '#dc3545';
            } else if (this.timeRemaining <= 120) {
                timerElement.style.color = '#ffc107';
            }
        }
    }

    getTimeRemaining() {
        return this.timeRemaining;
    }
}

// Quiz Manager
class QuizManager {
    constructor(quizId) {
        this.quizId = quizId;
        this.questions = [];
        this.timer = null;
    }

    async loadQuiz() {
        try {
            const quiz = await API.getQuiz(this.quizId);
            this.questions = quiz.questions;
            this.renderQuiz(quiz);
            return true;
        } catch (error) {
            console.error('Error loading quiz:', error);
            this.showError('Failed to load quiz. Please try again.');
            return false;
        }
    }

    renderQuiz(quiz) {
        const wrapper = document.getElementById('questions-wrapper');
        if (!wrapper) return;

        let html = '';
        this.questions.forEach((question, index) => {
            html += `
                <div class="question-card" data-question-id="${question.id}">
                    <h3>Question ${index + 1} of ${this.questions.length}</h3>
                    <p class="question-text">${this.escapeHtml(question.text)}</p>
                    <div class="choices">
                        ${question.choices.map(choice => `
                            <label class="choice-label">
                                <input type="radio" name="question_${question.id}" value="${choice.id}">
                                <span class="choice-text">${this.escapeHtml(choice.text)}</span>
                            </label>
                        `).join('')}
                    </div>
                </div>
            `;
        });

        wrapper.innerHTML = html;

        // Hide loading, show form
        const loading = document.getElementById('loading');
        const form = document.getElementById('quiz-form');
        if (loading) loading.style.display = 'none';
        if (form) form.style.display = 'block';

        // Start timer
        this.startTimer(600); // 10 minutes
    }

    startTimer(seconds) {
        this.timer = new QuizTimer(seconds, () => {
            this.submitQuiz();
        });
        this.timer.start();
    }

    collectAnswers() {
        const answers = {};
        const questionCards = document.querySelectorAll('.question-card');

        questionCards.forEach(card => {
            const questionId = card.dataset.questionId;
            const selected = card.querySelector('input[type="radio"]:checked');
            if (selected) {
                answers[questionId] = parseInt(selected.value);
            }
        });

        return answers;
    }

    async submitQuiz() {
        if (this.timer) {
            this.timer.stop();
        }

        const answers = this.collectAnswers();

        // Check if all questions are answered
        const answeredCount = Object.keys(answers).length;
        if (answeredCount < this.questions.length) {
            const confirmSubmit = confirm(
                `You have only answered ${answeredCount} out of ${this.questions.length} questions. ` +
                `Are you sure you want to submit?`
            );
            if (!confirmSubmit) {
                this.startTimer(this.timer.getTimeRemaining());
                return;
            }
        }

        try {
            const result = await API.submitQuiz(this.quizId, answers);
            window.location.href = `/result/${result.score_id}`;
        } catch (error) {
            console.error('Error submitting quiz:', error);
            alert('Failed to submit quiz. Please try again.');
            this.startTimer(this.timer.getTimeRemaining());
        }
    }

    showError(message) {
        const loading = document.getElementById('loading');
        if (loading) {
            loading.innerHTML = `<p class="error">${this.escapeHtml(message)}</p>`;
        }
    }

    escapeHtml(text) {
        const div = document.createElement('div');
        div.textContent = text;
        return div.innerHTML;
    }
}

// Initialize Quiz if on quiz page
document.addEventListener('DOMContentLoaded', function () {
    const quizForm = document.getElementById('quiz-form');
    if (quizForm) {
        const submitBtn = document.getElementById('submit-quiz');
        if (submitBtn) {
            submitBtn.addEventListener('click', () => {
                const quizId = {{ quiz.id }
            };
            const manager = new QuizManager(quizId);
            manager.submitQuiz();
        });
        }
    }
});

// Utility Functions
function showAlert(message, type = 'error') {
    const alertDiv = document.createElement('div');
    alertDiv.className = `alert alert-${type}`;
    alertDiv.textContent = message;

    const container = document.querySelector('.main-content .container');
    if (container) {
        container.insertBefore(alertDiv, container.firstChild);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            alertDiv.remove();
        }, 5000);
    }
}

function formatDate(dateString) {
    const date = new Date(dateString);
    return date.toLocaleDateString('en-US', {
        year: 'numeric',
        month: 'short',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit'
    });
}

// Export for use in other scripts
window.QuizApp = {
    API,
    QuizTimer,
    QuizManager,
    showAlert,
    formatDate
};
