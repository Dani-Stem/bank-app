import random

class Bank_account:
    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance
    
    def deposit(self):
        deposit_amount = input("How much are you depositing: ")
        self.balance += deposit_amount

def start():
    print("Welcome to The Dani Bank")
    print("what would you like to do?")
    print("a. create account b. access account")
    user_input = input("Option Selection: ")

    if user_input == "a":
        create_account()

def create_account():
    number = random.randint(100,200)
    owner = input("Please Provide your full name: ")

    print("New account Number: " + str(number))
    print("Account Holder " + str(owner))
    print("would you like to make a deposit? ")
    make_deposit = input("type y or n: ")


if __name__ == "__main__":
    start()
