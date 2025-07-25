from flask import Blueprint, render_template, request, redirect, url_for, session
from .models import db, User, Question, Attempt

bp = Blueprint('main', __name__)

# Sınav sorularını veritabanına ekleme (ilk açılışta)
@bp.before_app_request
def seed_questions():
    if Question.query.count() == 0:
        qs = [
            ("Discord.py ile sohbet botu otomasyonu nasıl gerçekleştirilir?", 
             {'A': 'Komut tabanlı event handling', 'B': 'HTTP istekleri', 'C': 'GUI olayları', 'D': 'Dosya işlemleri'}, 'A'),
            ("Flask uygulamasında route tanımlama nasıl yapılır?", 
             {'A': '@flask.route', 'B': '@app.route', 'C': '@db.route', 'D': '@model.route'}, 'B'),
            ("Yapay zeka modellerini eğitirken hangi kütüphane yaygın olarak kullanılır?", 
             {'A': 'Requests', 'B': 'TensorFlow', 'C': 'Pandas', 'D': 'BeautifulSoup'}, 'B'),
            ("Bilgisayar görüşü projelerinde hangi kütüphane sıklıkla tercih edilir?", 
             {'A': 'ImageAI', 'B': 'NLTK', 'C': 'Flask', 'D': 'Matplotlib'}, 'A'),
            ("Doğal Dil İşleme için hangi Python kütüphanesi uygundur?", 
             {'A': 'Scikit-learn', 'B': 'NLTK', 'C': 'Django', 'D': 'SQLAlchemy'}, 'B'),
        ]
        for text, choices, correct in qs:
            db.session.add(Question(text=text, choices=choices, correct=correct))
        db.session.commit()

@bp.route('/', methods=['GET', 'POST'])
def index():
    questions = Question.query.all()

    if request.method == 'POST':
        name = request.form.get('username').strip()
        if not name:
            return redirect(url_for('main.index'))

        user = User.query.filter_by(name=name).first()
        if not user:
            user = User(name=name)
            db.session.add(user)
            db.session.commit()

        # Puan hesaplama
        total = len(questions)
        correct_count = sum(1 for q in questions if request.form.get(f'question_{q.id}') == q.correct)
        score = int((correct_count / total) * 100)

        # Kayıt
        attempt = Attempt(score=score, user=user)
        db.session.add(attempt)
        db.session.commit()

        # *** Kullanıcıyı session’a kaydet ***
        session['user_id'] = user.id

        return redirect(url_for('main.result', user_id=user.id, attempt_id=attempt.id))

    # GET tarafı: session’daki user_id varsa çekelim
    user = None
    if session.get('user_id'):
        user = User.query.get(session['user_id'])

    global_best = db.session.query(db.func.max(Attempt.score)).scalar() or 0
    return render_template('index.html',
                           questions=questions,
                           global_best=global_best,
                           user=user)

@bp.route('/result')
def result():
    user_id = request.args.get('user_id', type=int)
    attempt_id = request.args.get('attempt_id', type=int)
    user = User.query.get_or_404(user_id)
    attempt = Attempt.query.get_or_404(attempt_id)
    global_best = db.session.query(db.func.max(Attempt.score)).scalar() or 0

    return render_template('result.html',
                           user=user,
                           attempt=attempt,
                           global_best=global_best)
