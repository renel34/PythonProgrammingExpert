class BankAccount:
    def __init__(self, account_holder_name):
        self.account_holder_name = account_holder_name
        self._balance = 0

    @property
    def balance(self):
        return round(self._balance)

    @balance.setter
    def balance(self, balance):
        if type(balance) == int or type(balance) == float:
            if balance > 0 and balance < 100000:
                self._balance = balance
    
        
account = BankAccount("Clement")
account.balance = 99999
print(account.balance)