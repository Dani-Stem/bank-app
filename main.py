import random
import time

bank_accounts = {}

class Bank:
    def __init__(self, key, account_num, account_holder, account_balance):
        self.key = key
        self.account_num = account_num
        self.account_holder = account_holder
        self.account_balance = account_balance

def start(self):
    print("Welcome to Dani Bank")
    print("The Best Bank in the world")
    print("Please enter Account Holder Name or Number to continue")
    print("If you do not have an account press 0 to create one: ")
    user_input = input()

    if user_input == "0":
        self.create_account()

def create_account(self):
    print("Thank you for choosing Dani Bank")
    print("Please enter your name below: ")
    
    self.account_holder = input()
    self.account_num = random.randint(1000, 2000)
    self.key += 1
    self.account_balance = 1000

    print("Hello " + self.account_holder + "!")
    print("Your new account number is: " + self.account_num)
    print("Your current account balance is: " + self.account_balance)

    print("would you like to make a deposit?")
    user_input = input("type y or n: ")

    if user_input == "n":
        print("Okay, Thanks for choosing Dani Bank")
        print("I love you, Goodbye")
        exit()
    else:
        self.deposit()

    new_account = Bank(self.key, self.account_num, self.account_holder, self.account_balance)
    self.add_account(self.account_holder, new_account)
    return new_account

def add_account(key, value):
    bank_accounts[key] = value

def deposit(self):

    user_input = int(input("Please enter deposit amount: "))
    self.account_balance += user_input
    print("Your new balance is: " + self.account_balance)
    time.sleep(2)
    self.menu()

def withdraw(self):

    user_input = int(input("Please enter withdraw amount: "))
    self.account_balance -= user_input
    print("Your new balance is: " + self.account_balance)
    time.sleep(2)
    self.menu()

def menu(self):

    print("Hello " + self.account_holder + "!")
    print("Account number: " + self.account_num)
    print("Account balance: " + self.account_balance)

    print("would you like to make a deposit or withdraw?")
    user_input = input("Type d for deposite or w for withdraw: ")

    if user_input == "d":
        self.deposit()
    elif user_input == "w":
        self.withdraw()
    else: 
        print("Entry not recognized.")
        print("Please try again")
        print("...")
        time.sleep(2)
        self.menu()

if __name__ == "__main__":
    start()
