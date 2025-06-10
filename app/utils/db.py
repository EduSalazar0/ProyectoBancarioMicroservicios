import sqlite3
from flask import g

def get_db(app):
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(app.config['DB_PATH'])
    return db

def init_db(app):
    with app.app_context():
        db = get_db(app)
        cursor = db.cursor()

        # Tabla de clientes
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS clients (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password TEXT NOT NULL,
                full_name TEXT NOT NULL
            )
        ''')

        # Tabla de cuentas
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS accounts (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                client_id INTEGER,
                balance REAL DEFAULT 0,
                FOREIGN KEY (client_id) REFERENCES clients(id)
            )
        ''')

        db.commit()
