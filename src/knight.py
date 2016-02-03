from piece import piece
class knight(piece):
    
    def tag(self):
        if self.color == "white":
            return "wN"
        elif self.color == "black":
            return "bN"
    
    def attackedSquares(self):
        attacking = []
        finalAttacking = []
        attacking.append((self.rank + 1, self.file - 2))
        attacking.append((self.rank - 1, self.file - 2))
        attacking.append((self.rank + 1, self.file + 2))
        attacking.append((self.rank - 1, self.file + 2))
        attacking.append((self.rank + 2, self.file - 1))
        attacking.append((self.rank - 2, self.file - 1))
        attacking.append((self.rank + 2, self.file + 1))
        attacking.append((self.rank - 2, self.file + 1))
        
        for square in attacking:
            if (square[0] > 0 and square[0] < 9 and square[1] > 0 and square[1] < 9):
                finalAttacking.append(square)
                
        return finalAttacking
        