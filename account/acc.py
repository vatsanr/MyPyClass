
class Account:
    def __init__(self,filepath):
        self.filepath=filepath
        with open(filepath,'r') as file:
            self.balance=int(file.read())

    def withdraw(self,amount):
        self.balance= self.balance - int(amount)

    def deposit(self,amount):
        self.balance=self.balance + int(amount)

    def commit(self):
        with open(self.filepath,'w') as file:
            file.write(str(self.balance))

class Checking(Account):
    def __init__(self,filepath,fee):
        self.fee=fee
        Account.__init__(self,filepath)

    def transfer(self,amount):
        self.balance=self.balance - amount - self.fee

checking=Checking("account/balance.txt",1)
print(checking)
print(checking.balance)
checking.withdraw(100)
checking.transfer(100)
print(checking.balance)
checking.deposit(100)
print(checking.balance)
checking.commit()
