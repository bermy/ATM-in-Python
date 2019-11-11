import sys

class InsertPasswordState:

    def __init__(self, atmMachine):
        pw = (input("Please enter your password or press q to quit: ")) # todo add quit option
        # dealing with non-existing passwords
        if pw in atmMachine.users.keys():
            atmMachine.currentUser = pw
            print("Success!\n")
            atmMachine.setMenuState()
        elif pw == "q":
            self.quit()
        else:
            print("Wrong or invalid input. Please try again\n")
            atmMachine.setInsertPasswordState()

    def quit(self):
        sys.exit()
