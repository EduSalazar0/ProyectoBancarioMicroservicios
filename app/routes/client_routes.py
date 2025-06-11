from flask import Blueprint, render_template, session, redirect, url_for, request, flash
from app.services.client_service import ClientService
from flask import current_app as app
from app.utils.client_context import get_client_context

client_bp = Blueprint('client_bp', __name__)
client_service = ClientService(app)

@client_bp.route('/client/account')
def client_account():
    context = get_client_context()
    if not context:
        return redirect(url_for('auth_bp.login'))

    account = client_service.get_client_account_info(context['client_id'])

    return render_template('client_account.html', client_name=context['client_name'], account=account)


@client_bp.route('/client/deposit', methods=['GET', 'POST'])
def client_deposit():
    context = get_client_context()
    if not context:
        return redirect(url_for('auth_bp.login'))

    if request.method == 'POST':
        try:
            amount = float(request.form['amount'])
            if amount <= 0:
                flash('El monto debe ser mayor que 0.', 'error')
            else:
                client_service.deposit(context['client_id'], amount)
                flash(f'Se depositaron ${amount:.2f} correctamente.', 'success')
                return redirect(url_for('client_bp.client_account'))
        except ValueError:
            flash('Por favor ingrese un monto válido.', 'error')

    return render_template('client_deposit.html', client_name=context['client_name'])


@client_bp.route('/client/transactions')
def client_transactions():
    context = get_client_context()
    if not context:
        return redirect(url_for('auth_bp.login'))

    transactions = client_service.get_transactions(context['client_id'])

    return render_template('client_transactions.html', client_name=context['client_name'], transactions=transactions)
