from abc import ABC

class Token(ABC):
    """This class is an abstract definition of a tetris token from which will be defined the rest of the token tipes"""
    def __init__(self,x,y):
        self.xPos = x   #Position X of the token
        self.yPos = y  #Position Y of the token
        self.dir = 0; #Direction of the token (being 0 up, 1 right, 2 down and 3 left )
    
    def  rotateRight(self):
        """This method rotates the token to the right"""
        if(self.dir == 3):
            self.dir = 0
        else:
            self.dir += 1
    
    def  rotateLeft(self):
        """This method rotates the token to the left"""
        if(self.dir == 0):
            self.dir = 3
        else:
            self.dir -= 1
            
    def moveRigth(self):
        """This method moves the tile right 1 unit"""
        self.xPos += 1

    def moveLeft(self):
        """This method moves the tile left 1 unit"""
        self.xPos -= 1
    
    def moveDown(self):
        """This method moves the tile down 1 unit"""
        self.yPos += 1

class Square(Token):
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return []
        elif(self.dir == 1):
            return []
        elif(self.dir == 2):
            return []
        elif(self.dir == 3):
            return []
        
class Line(Token):
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return []
        elif(self.dir == 1):
            return []
        elif(self.dir == 2):
            return []
        elif(self.dir == 3):
            return [] 
        
class RigthS(Token):
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return []
        elif(self.dir == 1):
            return []
        elif(self.dir == 2):
            return []
        elif(self.dir == 3):
            return []
        
class LeftS(Token):
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return []
        elif(self.dir == 1):
            return []
        elif(self.dir == 2):
            return []
        elif(self.dir == 3):
            return []
        
class RightL(Token):
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return []
        elif(self.dir == 1):
            return []
        elif(self.dir == 2):
            return []
        elif(self.dir == 3):
            return []
        
class LeftL(Token):
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return []
        elif(self.dir == 1):
            return []
        elif(self.dir == 2):
            return []
        elif(self.dir == 3):
            return []