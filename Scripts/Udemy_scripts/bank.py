#!/usr/bin/env python3

'''
Creation of a bank account and method that specifies name, balance and minimum balance.
deposit method allows additions to be made, variable amount.
withdraw method allows removal of funds, via variable amount.
   - Withdrawals cannot exceed total balance, triggers else statement
statement method allows for balance to be printed.
'''

class Account:
    def __init__(self, name, balance, min_balance):
        self.name = name
        self.balance = balance
        self.min_balance = min_balance
    
    def deposit(self,amount):
        self.balance += amount

    def withdraw(self,amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount
        else:
            print("Sorry you don't have enough funds")
    
    def statement(self):
        print("Account Balance: £{}".format(self.balance))

'''
Current account class allows for overdraft not exceeding 1000.
Polymorph of the Account class, and all methods from account can be used against it.
'''

class Current(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = -1000)
    
    def __str__(self):
        return "{}'s Current Account: Balance £{}".format(self.name,self.balance)
    
'''
Savings account class allows for no overdraft.
Polymorph of the Account class, and all methods from account can be used against it.
'''

class Savings(Account):
    def __init__(self,name,balance):
        super().__init__(name,balance,min_balance = 0)
    
    def __str__(self):
        return "{}'s Savings Account: Balance £{}".format(self.name,self.balance)
