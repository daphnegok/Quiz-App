# Quiz-App

Bu proje, Flask ve SQLAlchemy kullanarak geliştirilmiş bir quiz uygulamasıdır.

## Gereksinimler

* Python 3.7 ve üstü
* pip

## Kurulum ve Çalıştırma

Aşağıdaki adımları izleyerek proje ortamını oluşturabilir, bağımlılıkları yükleyebilir ve uygulamayı çalıştırabilirsiniz.

```bash
# 1. Depoyu klonlayın ve proje dizinine geçin
git clone <REPO_URL>
cd quiz_app

# 2. Sanal ortam oluşturun
# Windows (PowerShell veya CMD) kullanıyorsanız:
py -3 -m venv venv

# 3. Sanal ortamı etkinleştirin
# Windows CMD:
venv\Scripts\activate.bat
# Windows PowerShell:
.\venv\Scripts\Activate.ps1
# macOS/Linux:
source venv/bin/activate

# 4. pip'i güncelleyin ve bağımlılıkları yükleyin
pip install --upgrade pip
pip install -r requirements.txt

# 5. Uygulamayı çalıştırın
# Seçenek A: Doğrudan python ile
python run.py

# Seçenek B: Flask CLI ile
# macOS/Linux:
export FLASK_APP=run.py
flask run
# Windows CMD:
set FLASK_APP=run.py
flask run
# Windows PowerShell:
$Env:FLASK_APP = "run.py"
flask run

# Sunucuya tarayıcıdan erişim:
# http://127.0.0.1:5000/
```

## Ortamı Kapatmak

```bash
# Sanal ortamı devre dışı bırakmak için:
deactivate
```

---

