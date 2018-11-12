from Token import *
import numpy as np

class Colors:
    """Class that returns the color of the background for an specific color tile"""
    BLACK = "\u001b[40;1m"
    RED = "\u001b[41;1m"
    WHITE = "\u001b[47;1m"
    PURPLE = "\u001b[45;1m"
    BLUE = "\u001b[44;1m"
    GREEN = "\u001b[42;1m"
    YELLOW = "\u001b[43;1m"
    CYAN = "\u001b[46;1m"
    RESET = "\u001b[0m"
    
    def getColor(self , num):
        if(num == 0):
            return self.BLACK + " " + self.RESET
        elif(num == 1):
            return self.RED + " " + self.RESET
        elif(num == 2):
            return self.WHITE + " " + self.RESET
        elif(num == 3):
            return self.PURPLE + " " + self.RESET
        elif(num == 4):
            return self.BLUE + " " + self.RESET
        elif(num == 5):
            return self.GREEN + " " + self.RESET
        elif(num == 6):
            return self.YELLOW + " " + self.RESET
        elif(num == 7):
            return self.CYAN + " " + self.RESET
    

class Board():
    
    def __init__(self):        
        self.tiles = np.full((20, 10), 0)
        
    def printBoard(self):
        """Prints the board in the console"""
        for i in self.tiles:
            for j in i:
                print(Colors.getColor(Colors,j))
            print(".\n")
            
        