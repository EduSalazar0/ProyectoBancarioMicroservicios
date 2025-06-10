from app.utils.db import get_db

class ClientService:
    def __init__(self, app):
        self.app = app

    def get_client_account_info(self, client_id):
        db = get_db(self.app)
        cursor = db.cursor()

        cursor.execute('''
            SELECT balance
            FROM accounts
            WHERE client_id = ?
        ''', (client_id,))
        result = cursor.fetchone()

        if result:
            return result[0]  # balance
        else:
            return 0.0

    def deposit(self, client_id, amount):
        db = get_db(self.app)
        cursor = db.cursor()

        # Actualizar el saldo
        cursor.execute('''
            UPDATE accounts
            SET balance = balance + ?
            WHERE client_id = ?
        ''', (amount, client_id))

        db.commit()
