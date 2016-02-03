from piece import piece

class board(object):
    
    
    def __init__(self):
        self.squares = [[], [], [], [], [], [], [], []]
        self.pieces = []
        for rank in self.squares:
            for x in range(0,8):
                rank.append(None)
                
    def getSquares(self):
        print self.squares
    
    def getPiece(self, position):
        return self.squares[position[0] - 1][position[1] - 1]
    
    def movePiece(self, piece, newPosition):
        capturedPiece = self.squares[newPosition[0] - 1][newPosition[1] - 1]
        if capturedPiece == None:
            self.squares[newPosition[0] - 1][newPosition[1] - 1] = piece
            piecePosition = piece.getPosition()
            self.squares[piecePosition[0] - 1][piecePosition[1] - 1] = None
            return True
        elif capturedPiece.getColor() == piece.getColor():
            print "You are trying to capture your own piece, please choose another square."
            return False
        elif capturedPiece.getColor() != piece.getColor():
            toDelete = self.getPiece(newPosition)
            self.pieces.remove(toDelete)
            self.squares[newPosition[0] - 1][newPosition[1] - 1] = None
            self.squares[newPosition[0] - 1][newPosition[1] - 1] = piece
            piecePosition = piece.getPosition()
            self.squares[piecePosition[0] - 1][piecePosition[1] - 1] = None
            print 
            return True
        else:
            raise ValueError('Else case in move piece, please check movePiece under board.py.')
            return False
    
    def placePiece(self, position, piece):
        self.squares[position[0] - 1][position[1] - 1] = piece #subtractions are for adjustments between array 0's and 1's
        self.pieces.append(piece)
    

    def getAttacked(self):
        attackedSquares = [[], [], [], [], [], [], [], []]
        for rank in attackedSquares:
            for x in range(0,8):
                rank.append(0)
        for piece in self.pieces:
            for square in piece.attackedSquares():
                position = piece.getPosition()
                if piece.getColor() == "white":
                    attackedSquares[square[0] - 1][square[1] - 1] += 1

                elif piece.getColor() == "black":
                    attackedSquares[square[0] - 1][square[1] - 1] -= 1
                    
        return attackedSquares
        
    def isFull(self, position):
        return not self.squares[position[0] - 1][position[1] - 1] == None
        #if the given position has a piece return true
        
    def printBoard(self):
        printBoard = [[], [], [], [], [], [], [], []]
        for rank in printBoard:
            for x in range(0,8):
                rank.append("XX")
        for piece in self.pieces:
            piecePosition = piece.getPosition()
            printBoard[piecePosition[0] - 1][piecePosition[1] - 1] = piece.tag()
            
        return printBoard
        