import sys
from InsertPasswordState import InsertPasswordState


class NotLoggedInState:

    def __init__(self, atmMachine):
        print("\nWelcome to Yoav's ATM\n")
        option = (input("To Login Press 1. \nTo Quit press 2.\n"))
        if option == "1":
            atmMachine.state = InsertPasswordState(atmMachine)
        elif option == "2":
            self.quit()
        else:
            print("ERROR: Invalid input. Try again.")
            atmMachine.state = NotLoggedInState(atmMachine)

    def quit(self):
        sys.exit()
