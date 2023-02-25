class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def set_balance(self, balance):
        if type(balance) == int or type(balance) == float:
            if balance > 0 and balance < 100000:
                self._balance = balance
    
    def get_balance(self):
        return round(self._balance)
    
account = BankAccount("Clement")
account.set_balance(56.6)
print(account.get_balance())