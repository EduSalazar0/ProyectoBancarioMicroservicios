import sqlite3

db_path = 'proyecto_bancario.db'

conn = sqlite3.connect(db_path)
conn.close()

print("proyecto_bancario.db creado vacío.")
