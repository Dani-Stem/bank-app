import random
import FreeSimpleGUI as sg

sg.theme('DarkAmber')

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

        while True:

            layout = [  [sg.Text("Welcome to The Dani Bank")],
                        [sg.Text("What would you like to do?")],
                        [sg.Button("Create account"), sg.Button("Access account"), sg.Exit()]]

            # Create the Window
            window = sg.Window('Window Title', layout)
            # Event Loop to process "events"
            while True:
                event, values = window.read()
                if event in (sg.WIN_CLOSED, 'Exit'):
                    break

                elif event in (sg.WIN_CLOSED, 'Create account'):
                    
                    window.close()

                    if self.account is None:

                        # If no account exists, allow user to create one
                        self.create_account()
                        break
                    # else:
                    #     # If an account already exists, this prevents creation of another
                    #     print("Account already exists")
                    #     user_input = input("Would you like to access your account? (y/n): ")
                    #     if user_input == "y":
                    #         self.access_account()
                    #         break
                    #     else:
                    #         self.main()
                    #         break
                    
                elif event in (sg.WIN_CLOSED, 'Access account'):
                    
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
                        self.access_account()
                        break
           
    def create_account(self):

        self.number = random.randint(1000, 2000)

        layout = [[sg.Text("Please provide your full name: ")],
                [sg.InputText()],
                [sg.Button('Enter'), sg.Button('Cancel')] ]

        window = sg.Window('Window Title', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Enter'):
            self.owner = sg.InputText
            window.close()

            self.account = Account(self.number, self.owner)

            layout = [[sg.Text("New account number: " + str(self.number))],
                    [sg.Text("Account holder: " + str(self.owner))],
                    [sg.Text("Would you like to make a deposit?")],
                    [sg.Button('Yes'), sg.Button('No')] ]

            window = sg.Window('Window Title', layout)

            event, values = window.read()

            while True:
                if event in (sg.WIN_CLOSED, 'Yes'):
                        window.close()
                        self.deposit()
                elif event in (sg.WIN_CLOSED, 'No'):
                    
                    window.close()
                    layout = [[sg.Text("Thank you for creating an account with us.")],
                            [sg.Button('Exit')]]

                    window = sg.Window('Window Title', layout)

                    event, values = window.read()

                    if event in (sg.WIN_CLOSED, 'Exit'):
                        window.close()
                        quit()

            # print("New account number: " + str(self.number))
            # print("Account holder: " + str(self.owner))
            # print("Would you like to make a deposit?")

            # decision = input("Type y or n: ")

            # This loop keeps running until the user enters a valid response (y or n)
            # while True:
            #     if decision == "y":
            #         self.deposit()
            #         break
            #     elif decision == "n":
            #         print("Thank you for creating an account with us.")
            #         self.main()
            #         break
            #     else:
            #         print("Invalid option. Please try again.")
            #         decision = input("Please type y or n: ")

    def access_account(self):
        layout = [[sg.Text(f"Welcome back, {self.account.owner}!")],
                [sg.Text(f"Your current balance is: ${self.account.check_balance()}")], 
                [sg.Text("Would you like to make a deposit or withdraw?")],
                [sg.Button('deposit')], [sg.Button('withdraw')], [sg.Button('Exit')]]

        window = sg.Window('Window Title', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'deposit'):
            window.close()
            self.deposit()
            # break

        if event in (sg.WIN_CLOSED, 'withdraw'):
            window.close()

            layout = [[sg.Text("Enter amount to withdraw: ")],
                    [sg.InputText()],
                    [sg.Button('Enter'), sg.Button('Cancel')] ]

            window = sg.Window('Window Title', layout)

            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Enter'):
                window.close()

                amount = float(values[0])

                self.withdraw(amount)

                # Uses the withdraw method/function from the Account class
                result = self.account.withdraw(amount)

                # Checks if the withdrawal was successful
                if result == "Insufficient funds":
                    print(result)
                else:
                    print(f"New balance: ${result}")

                self.main()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            self.exit()
            # break

    def deposit(self):
        layout = [[sg.Text("How much are you depositing: ")],
                [sg.InputText()],
                [sg.Button('Enter'), sg.Button('Cancel')] ]

        window = sg.Window('Window Title', layout)

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

                    window = sg.Window('Window Title', layout)

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

            window = sg.Window('Window Title', layout)

            event, values = window.read()

            if event in (sg.WIN_CLOSED, 'Ok'):
                window.close()
                self.main()
                self.deposit()
                # break

        # Deposit using the Account class's method/function
        self.account.deposit(amount)

        # Uses the check_balance method/function from the Account class to show the new balance

        balance = self.account.check_balance()

        layout = [[sg.Text("New balance: $" + str(balance))],
                [sg.Button('Back to Menu')], [sg.Button('Exit')]]

        window = sg.Window('Window Title', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            self.exit()
            window.close()
            # self.main()
            # self.deposit()
            # break



        if event in (sg.WIN_CLOSED, 'Back to Menu'):
            self.main()
            window.close()

    def exit(self):
                    
        layout = [[sg.Text("Thank you for banking with us. Goodbye!")],
                [sg.Button('Exit')]]

        window = sg.Window('Window Title', layout)

        event, values = window.read()

        if event in (sg.WIN_CLOSED, 'Exit'):
            window.close()
            self.main()
            quit()


start = Bank()
