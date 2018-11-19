

class AI:
    def getYpos(Token, tiles):
        "Returns the Y downest posible position for a  given token in its X coordinate and orientation"
        countY = 19
        found = False
        while(countY >= 0 && !found):
            good = True
            for i in Token.getForm():
                if(tiles[i[1]][i[0]] != 0):
                    good = False
            if(good):
                found = True
            else:
                countY -= 1
        return countY

    def evalNewMove(Token, tiles):
        """Returns the value of a movement relative to the board (befor playing it)"""
        if(!checkValidPosition(Token)):
            return -100 #if the position is not valid a bad evaluation is given
        for i in Token.getForm(): #the move is written on the board
            tiles[i[1]][i[0]] = -1
        value = 0
        forj in tiles:
            linecount = 1
            for i in j:
                if(tiles[j][i] == - 1):
                    value += linecount
                    linecount++
        for i in range 10:
            penalty = -1
            posibleGap = False #indicates if there is a gap under a token (this is bad)
            for j in tiles:
                if(posibleGap && tiles[j][i] == 0):
                    value += penalty
                    penalty * 2 #the penalty is increased a lot to be sure that this move is not selected
                if(tiles[j][i] == -1): #this means that if under it there is a gap is a penalty
                    posibleGap = True
        return value

    def checkValidPosition(Token):
        """checks of the position of the token is valid and is inside the board"""
        for i in Token.getForm():
            if(i[0] < 0 || > 9):
                return False
            elif(i[1] < 0 || > 19):
                return False
            else
                return True

    def treeSearch(actualToken, nextToken): #make recursive ??
        """makes a montecarlo tree search of the best outcome"""
