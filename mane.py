import random

bank_accounts = {}

class Bank_account:

    def __init__(self, number, owner, balance):
        self.number = number
        self.owner = owner
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdrawl(self, amount):
        self.balance -= amount
    
    def check_balance(self):
        return self.balance

def start():
    print("Welcome to The Dani Bank")
    print("what would you like to do?")
    print("a. create account b. access account")
    user_input = input("Option Selection: ")
    account = None

    if user_input == "a":
        account = create_account()
    elif user_input == "b":
        account_name = input("Account Owner: ")
        account = get_account(account_name)
        print("what would you like to do?")
        print("a.view balance b. deposite c. withdrawl ")
        user_input = input("Option Selection: ")
        
        if user_input == "a":
            account.check_balance()
        elif user_input == "b":
            amount = int(input("How much: "))
            account.deposit(amount)
        elif user_input == "c":
            amount = int(input("How much: "))
            account.withdrawl(amount)

    return account

def create_account():
    number = random.randint(100,200)
    owner = input("Please Provide your full name: ")

    print("New account Number: " + str(number))
    print("Account Holder: " + str(owner))
    print("would you like to make a deposit? ")
    initial_deposit = 0
    make_deposit = input("type y or n: ")

    if make_deposit == "y":
        initial_deposit = int(input("How much: "))
    else:
        print("okay, Goodbye.")
        exit()

    new_account = Bank_account(number, owner, initial_deposit)

    add_account(owner, new_account)
    
    return new_account

def add_account(key, value):
    bank_accounts[key] = value

def get_account(key):
    return bank_accounts[key]

if __name__ == "__main__":
  
    while True:
        i = start()
        print("New Balance for Account " + i.owner + ":" + str(i.check_balance()))  

        # print("Who has accounts in Dani's Bank and how much")
        # for key, value in bank_accounts.items():
        #     print(key + " - " + str(value.check_balance()))

    # accountA = start()
    # print("New Balance for Account A: " + str(accountA.check_balance()))

    # accountB = start()
    # print("New Balance for Account B: " + str(accountB.check_balance()))

    # accountC = start()
    # print("Checking balance for: " + accountC.owner + " - " + str(accountC.check_balance()))


    