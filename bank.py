import random
import tkinter as tk
from tkinter import *


# The Bank class uses this Account class to create and access an account
class Account:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance


# Main class
class Bank:
    def __init__(self):
        self.number = 0
        self.owner = ""
        self.account = None
        self.main()  # Starts the main menu when the program starts

    def main(self):

        
        print("Welcome to The Dani Bank")
        print("What would you like to do?")
        print("a. Create account   b. Access account   c. Exit")

        user_input = input("Option Selection: ")

        # This loop runs forever until we "break"(stop the while loop)
        # It's used to keep asking the user until they enter a valid option
        while True:
            if user_input == "a":
                if self.account is None:
                    # If no account exists, allow user to create one
                    self.create_account()
                    break
                else:
                    # If an account already exists, this prevents creation of another
                    print("Account already exists")
                    user_input = input("Would you like to access your account? (y/n): ")
                    if user_input == "y":
                        self.access_account()
                        break
                    else:
                        self.main()
                        break

            elif user_input == "b":
                # If user tries to access account without one existing
                if self.account is None:
                    print("No account found. Please create an account first.")
                    user_input = input("Would you like to create an account? (y/n): ")
                    if user_input == "y":
                        self.create_account()
                        break
                    else:
                        self.main()
                        break
                else:
                    # If an account exists, this allows user to access it
                    self.access_account()
                    break

            elif user_input == "c":
                self.exit()  # Calls the exit method/function and quits the program
                break

            else:
                # If the user enters something that's not a, b, or c
                print("Invalid option. Please try again.")
                user_input = input("Option Selection: ")

                

    def create_account(self):
        self.number = random.randint(1000, 2000)
        self.owner = input("Please provide your full name: ")

        # Creates a new account using the Account class
        self.account = Account(self.number, self.owner)

        print("New account number: " + str(self.number))
        print("Account holder: " + self.owner)
        print("Would you like to make a deposit?")

        decision = input("Type y or n: ")

        # This loop keeps running until the user enters a valid response (y or n)
        while True:
            if decision == "y":
                self.deposit()
                break
            elif decision == "n":
                print("Thank you for creating an account with us.")
                self.main()
                break
            else:
                print("Invalid option. Please try again.")
                decision = input("Please type y or n: ")

    def access_account(self):
        # Accesses the owner variable from the Account class
        print(f"Welcome back, {self.account.owner}!")
        # Uses the check_balance method/function from the Account class
        print(f"Your current balance is: ${self.account.check_balance()}")
        print("Would you like to make a deposit or withdraw?")

        user_input = input("a. deposit   b. withdraw   c. back: ")

        while True:  # Loops until user makes a valid choice
            if user_input == "a":
                self.deposit()
                break

            elif user_input == "b":
                amount = float(input("Enter amount to withdraw: "))

                # Uses the withdraw method/function from the Account class
                result = self.account.withdraw(amount)

                # Checks if the withdrawal was successful
                if result == "Insufficient funds":
                    print(result)
                else:
                    print(f"New balance: ${result}")

                self.main()
                break

            elif user_input == "c":
                self.main()
                break

            else:
                print("Invalid option. Please try again.")
                user_input = input("a. deposit   b. withdraw   c. back: ")

    def deposit(self):
        deposit_amount = input("How much are you depositing: ")

        # Tries to convert the input to a float (a float is a number with decimals)
        try:
            amount = float(deposit_amount)
        # If the input is not a number, show error and try again
        except ValueError:
            print("Invalid input. Please enter a number.")
            self.deposit()

        # Doesn't allow negative or zero deposits
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            self.deposit()

        # Deposit using the Account class's method/function
        self.account.deposit(amount)

        # Uses the check_balance method/function from the Account class to show the new balance
        balance = self.account.check_balance()
        print("New balance: $" + str(balance))

        self.main()

    def exit(self):
        print("Thank you for banking with us. Goodbye!")
        quit()



master = Tk()

def option_a():
    user_imput = "a"
    return user_imput

def option_b():
    user_imput = "b"
    return user_imput

Label(master, text='Welcome to The Dani Bank').grid(row=1)
Label(master, text='What would you like to do?').grid(row=2)
button = tk.Button(master, text='Create account', width=25, command=option_a).grid(row=3)
button = tk.Button(master, text='Access account', width=25, command=option_b).grid(row=3, column=1)
button = tk.Button(master, text='Exit', width=25, command=master.destroy).grid(row=3, column=2)
mainloop()

start = Bank()
