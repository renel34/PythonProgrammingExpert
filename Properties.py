class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    def set_balance(self, balance):
        if balance is not int:
            if balance < 0 or balance > 100000:
                raise ValueError("Enter number between 0 and 100,000!")
            self._balance = balance
    
    def get_balance(self):
        return round(self._balance)
    
account = BankAccount("Clement")
account.set_balance(100001)
print(account.get_balance())