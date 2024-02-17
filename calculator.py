class MyCalc:
    def __init__(self, fname, lname, balance = 0):
        self.firstname = fname
        self.lastname = lname
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self.balance
        else:
            return 'Sorry, you do not have sufficient funds to complete this operation'
        

demo_account = MyCalc('Joe','Blix')
print('Balance: ',demo_account.balance)

demo_account.deposit(100000)
print('Balance: ',demo_account.balance)

demo_account.withdraw(50000)
print('Balance: ',demo_account.balance)

