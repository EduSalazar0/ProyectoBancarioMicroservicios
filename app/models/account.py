class Account:
    def __init__(self, client_id, balance=0.0):
        self.client_id = client_id
        self.balance = balance

    def __repr__(self):
        return f"<Account client_id={self.client_id}, balance={self.balance}>"