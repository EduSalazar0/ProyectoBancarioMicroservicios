from flask import session
from app.utils.db import get_db
import sqlite3

class AuthService:
    def __init__(self, app):
        self.app = app

    def validate_login(self, username, password):
        db = get_db(self.app)
        cursor = db.cursor()

        try:
            cursor.execute("SELECT id, full_name FROM clients WHERE username=? AND password=?", (username, password))
            result = cursor.fetchone()

            if result:
                # Login exitoso → guardamos info en sesión
                session['client_id'] = result[0]
                session['client_name'] = result[1]
                return True
            else:
                return False

        except sqlite3.Error as e:
            print(f"Error en validate_login: {e}")
            return False
