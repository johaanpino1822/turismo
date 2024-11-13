from flask import Flask, render_template, redirect, url_for, request, session, flash
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = os.getenv('SECRET_KEY', 'clave_predeterminada_para_desarrollo')

@app.route('/')
def home():
    return redirect(url_for('main'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['user'] = request.form['email']
        flash("Inicio de sesión exitoso", "success")
        return redirect(url_for('main'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        session['user'] = request.form['email']
        flash("Registro exitoso", "success")
        return redirect(url_for('main'))
    return render_template('register.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/historia')
def historia():
    return render_template('historia.html')

@app.route('/sitio')
def sitio():
    return render_template('sitio.html')

@app.route('/hoteles')
def hoteles():
    if 'user' in session:
        return render_template('hoteles.html')
    else:
        flash("Debes iniciar sesión para acceder a la sección de hoteles.", "warning")
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Sesión cerrada", "info")
    return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)
