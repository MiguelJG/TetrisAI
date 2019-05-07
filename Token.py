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

    #@abstractmethod
    def tokenID(ABC):
        pass

class Square(Token):
    def tokenID():
        return 1

    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        return [[self.xPos, self.yPos], [self.xPos + 1, self.yPos], [self.xPos, self.yPos - 1], [self.xPos + 1, self.yPos - 1]]

class Line(Token):
    def tokenID():
        return 2
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0 or self.dir == 2):
            return [[self.xPos, self.yPos], [self.xPos, self.yPos - 1], [self.xPos, self.yPos - 2], [self.xPos, self.yPos - 3]]
        elif(self.dir == 1 or self.dir == 3):
            return [[self.xPos, self.yPos], [self.xPos + 1, self.yPos], [self.xPos + 2, self.yPos], [self.xPos + 3, self.yPos]]

class RigthS(Token):
    def tokenID():
        return 3
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0 or self.dir == 2):
            return [[self.xPos + 1, self.yPos], [self.xPos + 1, self.yPos - 1], [self.xPos, self.yPos - 1], [self.xPos, self.yPos - 2]]
        elif(self.dir == 1 or self.dir == 3):
            return [[self.xPos, self.yPos], [self.xPos + 1, self.yPos], [self.xPos + 1, self.yPos - 1], [self.xPos + 2, self.yPos - 1]]

class LeftS(Token):
    def tokenID():
        return 4
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0 or self.dir == 2):
            return [[self.xPos, self.yPos], [self.xPos, self.yPos - 1], [self.xPos + 1, self.yPos - 1], [self.xPos + 1, self.yPos - 2]]
        elif(self.dir == 1 or self.dir == 3):
            return [[self.xPos, self.yPos - 1], [self.xPos + 1, self.yPos - 1], [self.xPos + 1, self.yPos], [self.xPos + 2, self.yPos]]


class RightL(Token):
    def tokenID():
        return 5
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return [[self.xPos, self.yPos], [self.xPos + 1, self.yPos], [self.xPos, self.yPos - 1], [self.xPos, self.yPos - 2]]
        elif(self.dir == 1):
            return [[self.xPos, self.yPos], [self.xPos, self.yPos - 1], [self.xPos + 1, self.yPos - 1], [self.xPos + 2, self.yPos - 1]]
        elif(self.dir == 2):
            return [[self.xPos, self.yPos], [self.xPos, self.yPos - 1], [self.xPos, self.yPos - 2], [self.xPos + 1, self.yPos - 2]]
        elif(self.dir == 3):
            return [[self.xPos, self.yPos], [self.xPos + 1, self.yPos], [self.xPos + 2, self.yPos], [self.xPos + 2, self.yPos - 1]]

class LeftL(Token):
    def tokenID():
        return 6
    def getForm(self):
        """This method return the boxes of the board that are part of the token from its x,y position"""
        if(self.dir == 0):
            return [[self.xPos, self.yPos], [self.xPos + 1, self.yPos], [self.xPos + 1, self.yPos -1], [self.xPos + 1, self.yPos - 2]]
        elif(self.dir == 1):
            return [[self.xPos, self.yPos], [self.xPos, self.yPos - 1], [self.xPos + 1, self.yPos], [self.xPos + 2, self.yPos]]
        elif(self.dir == 2):
            return [[self.xPos, self.yPos], [self.xPos, self.yPos - 1], [self.xPos, self.yPos - 2], [self.xPos + 1, self.yPos - 2]]
        elif(self.dir == 3):
            return [[self.xPos, self.yPos - 1], [self.xPos + 1, self.yPos - 1], [self.xPos + 2, self.yPos - 1], [self.xPos + 2, self.yPos]]
