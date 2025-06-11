# app/utils/client_context.py

from flask import session

def get_client_context():
    """
    Retorna el contexto del cliente autenticado.
    Si no está autenticado, retorna None.
    """
    if 'client_id' not in session:
        return None

    return {
        'client_id': session.get('client_id'),
        'client_name': session.get('client_name')
    }
