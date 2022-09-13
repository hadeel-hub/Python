class User:
    def __init__(self,name):
        self.name= name
        self.account_balance=0
        
    def make_deposit(self,amount):
        self.account_balance+= amount
        return self
        
    def make_withdrawl(self,amount):
        self.account_balance-= amount
        return self
    def displayUser_account_balance(self):
      print(self.account_balance)
  
Rabab=User("rabab")

Rabab.make_deposit(3000).make_withdrawl(500).make_deposit(200).make_withdrawl(100)
Rabab.displayUser_account_balance()



    