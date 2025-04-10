class pawn:
    def __init__(self, pos1, pos2, colour, name):
        self.pos1 = pos1
        self.pos2 = pos2
        self.colour = colour
        self.name = name
        self.moved = False

        if colour == 'white':
             self.key = 12
        else: self.key = 6

    def check(self, dest1, dest2, pos1, pos2, state, flipped, left, right):
        if dest1 in range(8) and dest2 in range(8) and [dest1, dest2] in self.canMove(pos1, pos2, state, flipped, left, right):
            return True
        else:
            return False


    def canMove(self, pos1, pos2, state, flipped, left, right):
        # pos1 and pos2 are the position of the piece that is currently being investigated
        moves = []
    
        
        
        if pos1 in range(0,8) and pos2 - 1 in range(0,8):
            moves.append([pos1, pos2 - 1])

        if left and pos1 - 1 in range(0,8) and pos2 - 1 in range(0,8):
            moves.append([pos1 - 1, pos2 - 1])

        if right and pos1 + 1 in range(0,8) and pos2 - 1 in range(0,8):
            moves.append([pos1 + 1, pos2 - 1])
        
        if self.moved == False and state[pos1, pos2 - 2] == 0:
            moves.append([pos1, pos2 - 2])
        
                    

        return moves
    