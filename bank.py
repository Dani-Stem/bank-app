import random
import FreeSimpleGUI as sg
import sqlite3

conn = sqlite3.connect('accounts.db')

cursor = conn.cursor()

create_table_query = '''
CREATE TABLE IF NOT EXISTS accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Number INT NOT NULL UNIQUE,
    Owner TEXT NOT NULL,
    Balance INT
);
'''

cursor.execute("SELECT * FROM accounts")
all_users = cursor.fetchall()

print("All users in the database:")
for user in all_users:
    print(user)

conn.commit()

class Account:
    def __init__(self, number, owner):
        self.number = number
        self.owner = owner
        self.balance = 0

    def deposit(self, amount):

        self.balance += amount
        cursor.execute(f"UPDATE accounts SET Balance = {self.balance} WHERE Number = {self.number}")
        conn.commit()
        return self.balance

    def withdraw(self, amount):
        if amount > self.balance:
            return "Insufficient funds"
        else:
            self.balance -= amount
            return self.balance

    def check_balance(self):
        return self.balance

class Bank:
    def __init__(self):
        self.number = 0
        self.owner = ""
        self.account = None
        self.main() 

    def main(self):

        while True:

            layout = [  [sg.Text("Welcome to The Dani Bank")],
                        [sg.Text("What would you like to do?")],
                        [sg.Button("Create account"), sg.Button("Access account"), sg.Button("" \
                        "Exit")]]

            window = sg.Window('Dani Bank - Menu', layout)
            while True:
                event, values = window.read()
                if event in (sg.WIN_CLOSED, 'Exit'):
                    window.close()
                    self.exit()

                elif event in (sg.WIN_CLOSED, 'Create account'):
                    
                    window.close()

                    if self.account is None:

                        self.create_account()
                    
                elif event in (sg.WIN_CLOSED, 'Access account'):
                    window.close()
                    if self.account is None:
                    
                        self.number = random.randint(1000, 2000)

                        layout = [[sg.Text("No account found. Please create an account first.")],[sg.Text("Would you like to create an account?")],
                                [sg.Button('Yes'), sg.Button('Cancel')] ]

                        window = sg.Window('Create Account', layout)

                        event, values = window.read()

                        if event in (sg.WIN_CLOSED, 'Yes'):
                            window.close()
                            self.create_account()
                        if event in (sg.WIN_CLOSED, 'Cancel'):
                            window.close()
                            self.exit()
                    else:
                        self.access_account()
                        break
           
    def create_account(self):

        self.number = random.randint(1000, 2000)

        layout = [[sg.Text("Please provide your full name: ")],
                [sg.InputText(key="owner")],
                [sg.Button('Enter'), sg.Button('Cancel')] ]

        window = sg.Window('Create Account', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Enter'):
            self.owner = values["owner"]

            cursor.execute("INSERT INTO accounts (Number, Owner, Balance) VALUES (?, ?, ?)", (f"{self.number}", f"{self.owner}", "0"))

            conn.commit()

            window.close()

            self.account = Account(self.number, self.owner)

            layout = [[sg.Text("New account number: " + str(self.number))],
                    [sg.Text("Account holder: " + str(self.owner))],
                    [sg.Text("Would you like to make a deposit?")],
                    [sg.Button('Yes'), sg.Button('No')] ]

            window = sg.Window('Access Account', layout)

            event, values = window.read()

            while True:
                if event in (sg.WIN_CLOSED, 'Yes'):
                        window.close()
                        self.deposit()
                if event in (sg.WIN_CLOSED, 'No'):
                    
                    window.close()
                    layout = [[sg.Text("Thank you for creating an account with us.")],
                            [sg.Button('Exit')]]

                    window = sg.Window('Dani Bank - Goodbye', layout)

                    event, values = window.read()

                    if event in (sg.WIN_CLOSED, 'Exit'):
                        window.close()
                        quit()

    def access_account(self):
        layout = [[sg.Text(f"Welcome back, {self.account.owner}!")],
                [sg.Text(f"Your current balance is: ${self.account.check_balance()}")], 
                [sg.Text("Would you like to make a deposit or withdraw?")],
                [sg.Button('deposit')], [sg.Button('withdraw')], [sg.Button('Exit')]]

        window = sg.Window('Access Account', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'deposit'):
            window.close()
            self.deposit()

        if event in (sg.WIN_CLOSED, 'withdraw'):
            window.close()
            self.withdraw()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            self.exit()

    def deposit(self):
        layout = [[sg.Text("How much are you depositing: ")],
                [sg.InputText()],
                [sg.Button('Enter'), sg.Button('Cancel')] ]

        window = sg.Window('Deposit', layout)

        event, values = window.read()

        deposit_amount = values[0]
        window.close()

        # Tries to convert the input to a float (a float is a number with decimals)
        try:
            amount = float(deposit_amount)
        # If the input is not a number, show error and try again
        except ValueError:
                    layout = [[sg.Text("Invalid input. Please enter a number.")],
                            [sg.Button('Ok')]]

                    window = sg.Window('Deposit', layout)

                    event, values = window.read()

                    if event in (sg.WIN_CLOSED, 'Ok'):
                        window.close()
                        self.main()
                        self.deposit()
                        # break

        # Doesn't allow negative or zero deposits
        if amount <= 0:
            layout = [[sg.Text("Invalid amount. Please enter a positive number.")],
                    [sg.Button('Ok')]]

            window = sg.Window('Dani Bank - Error', layout)

            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Ok'):
                window.close()
                self.main()
                self.deposit()
                # break

        self.account.deposit(amount)

        balance = self.account.check_balance()

        layout = [[sg.Text("New balance: $" + str(balance))],
                [sg.Button('Back to Menu')], [sg.Button('Exit')]]

        window = sg.Window('Account Info', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            self.exit()


        if event in (sg.WIN_CLOSED, 'Back to Menu'):
            window.close()
            self.main()


    def withdraw(self):
        layout = [[sg.Text("How much are you withdrawing: ")],
                [sg.InputText()],
                [sg.Button('Enter'), sg.Button('Cancel')] ]

        window = sg.Window('Withdraw', layout)

        event, values = window.read()

        withdraw_amount = values[0]
        window.close()

        try:
            amount = float(withdraw_amount)

        except ValueError:
                    layout = [[sg.Text("Invalid input. Please enter a number.")],
                            [sg.Button('Ok')]]

                    window = sg.Window('Withdraw', layout)

                    event, values = window.read()

                    if event in (sg.WIN_CLOSED, 'Ok'):
                        window.close()
                        self.main()
                        self.withdraw()

        if amount <= 0:
            layout = [[sg.Text("Invalid amount. Please enter a positive number.")],
                    [sg.Button('Ok')]]

            window = sg.Window('Dani Bank - Error', layout)

            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Ok'):
                window.close()
                self.main()
                self.deposit()
                # break

        self.account.withdraw(amount)

        balance = self.account.check_balance()

        layout = [[sg.Text("New balance: $" + str(balance))],
                [sg.Button('Back to Menu')], [sg.Button('Exit')]]

        window = sg.Window('Account Info', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            self.exit()


        if event in (sg.WIN_CLOSED, 'Back to Menu'):
            window.close()
            self.main()

    def exit(self):
                    
        layout = [[sg.Text("Thank you for banking with us. Goodbye!")],
                [sg.Button('Exit')]]

        window = sg.Window('Dani Bank - Goodbye', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            conn.close()        
            quit()


start = Bank()
