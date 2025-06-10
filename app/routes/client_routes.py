from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from app.services.client_service import ClientService
from flask import current_app as app

client_bp = Blueprint('client_bp', __name__)
client_service = ClientService(app)

@client_bp.route('/client/account')
def client_account():
    if 'client_id' not in session:
        return redirect(url_for('auth_bp.login'))

    client_id = session.get('client_id')
    client_name = session.get('client_name')

    balance = client_service.get_client_account_info(client_id)

    return render_template('client_account.html', client_name=client_name, balance=balance)

@client_bp.route('/client/deposit', methods=['GET', 'POST'])
def client_deposit():
    if 'client_id' not in session:
        return redirect(url_for('auth_bp.login'))

    client_id = session.get('client_id')
    client_name = session.get('client_name')

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                flash('El monto debe ser mayor que 0.', 'error')
            else:
                client_service.deposit(client_id, amount)
                flash(f'Se depositaron ${amount:.2f} correctamente.', 'success')
                return redirect(url_for('client_bp.client_account'))
        except ValueError:
            flash('Por favor ingrese un monto válido.', 'error')

    return render_template('client_deposit.html', client_name=client_name)
