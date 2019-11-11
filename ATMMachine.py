import sys
from InsertPasswordState import InsertPasswordState
from MenuState import MenuState
from NotLoggedInState import NotLoggedInState
class ATMMachine:
    currentUser = ""
    users = {
        "1234" : 1500,
        "5678" : 200,
        "4321" : 500,
        "8765" : 10000,
    }
    def __init__(self):

        self.state = NotLoggedInState(self)

    #returns value of current user's balance
    def getVal(self):
        return self.users.get(self.currentUser, "none")

    def setNotLoggedInState(self):
        self.state = NotLoggedInState(self)

    def setMenuState(self):
        self.state = MenuState(self)

    def setInsertPasswordState(self):
        self.state = InsertPasswordState(self)

    def setMenuState(self):
        self.state = MenuState(self)

    def readInput(self):
        print(self.state.getStateOptions())


    def main(self):
        print("error")


    def requestMoney(self):
        print("error")


    def insertMoney(self):
        print("error")


    def checkBalance(self):
        print("error")


    def logoff(self):
        print("error")


    def quit(self):
        print("error")