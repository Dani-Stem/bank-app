import FreeSimpleGUI as sg

sg.theme('DarkAmber')   # Add a little color to your windows
# All the stuff inside your window. This is the PSG magic code compactor...
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

    if event in (sg.WIN_CLOSED, 'Access account'):
        
        print("Hello ")
        print("Account number: ")
        print("Account balance: ")


window.close()
