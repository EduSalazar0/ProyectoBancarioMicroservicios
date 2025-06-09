from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.services.auth_service import AuthService
from flask import current_app as app

auth_bp = Blueprint('auth_bp', __name__)

auth_service = AuthService(app)

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if auth_service.validate_login(username, password):
            flash('Login exitoso!', 'success')
            return redirect(url_for('auth_bp.client_home'))
        else:
            flash('Credenciales incorrectas. Intenta nuevamente.', 'danger')

    return render_template('login.html')

@auth_bp.route('/client/home')
def client_home():
    if 'client_id' not in session:
        return redirect(url_for('auth_bp.login'))

    client_name = session.get('client_name')
    return render_template('client_home.html', client_name=client_name)
  
@auth_bp.route('/')
def index():
    return redirect(url_for('auth_bp.login'))
