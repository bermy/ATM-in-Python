import sys

class MenuState:

    def __init__(self, atmMachine):
        option = (input("\nTo check your balance press 1\n""To deposit press 2 \nTo withdraw press 3\nTo logoff press 4\n"))
        if option == "1":
            self.checkBalance(atmMachine)
        elif option == "2":
            self.insertMoney(atmMachine)
        elif option == "3":
            self.requestMoney(atmMachine)
        elif option == "4":
            self.logoff(atmMachine)
        else:
            print("Wrong or invalid input. Please try again\n")
            atmMachine.setMenuState()

    def requestMoney(self, atmMachine):
        try:
            amount = float(input("Amount to withdraw:  "))
            if float(atmMachine.getVal() - float(amount)) < 0:
                print("You don't have enough balance for this action.\n")
                atmMachine.setMenuState()
            else:
                atmMachine.users[atmMachine.currentUser] -= amount
                print("Action completed were withdrawn.")
                atmMachine.setMenuState()
        except ValueError:
            print("Please use numbers.")
            atmMachine.setMenuState()

    def insertMoney(self, atmMachine):
        try:
            amount = float(input("Amount to deposit:  "))
            newAmount = float(amount) + atmMachine.users[atmMachine.currentUser]
            atmMachine.users[atmMachine.currentUser] = newAmount
            print("New balance is: " + str(atmMachine.users[atmMachine.currentUser]))
            atmMachine.setMenuState()
        except ValueError:
            print("not a number")
            atmMachine.setMenuState()

    def checkBalance(self, atmMachine):
        print("User: " + atmMachine.currentUser + "\nBalance: " + str(atmMachine.getVal()))
        atmMachine.setMenuState()

    def logoff(self, atm):
        print("Account logged off! \n")
        atm.setNotLoggedInState()

    def quit(self):
        sys.exit()
