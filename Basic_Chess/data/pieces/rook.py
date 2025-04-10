class rook:
    def __init__(self, pos1, pos2, colour, name):
        self.pos1 = pos1
        self.pos2 = pos2
        self.colour = colour
        self.name = name

        if colour == 'white':
             self.key = 1
        else: self.key = 7

    def check(self, dest1, dest2, pos1, pos2, state, flipped):
        if dest1 in range(8) and dest2 in range(8) and [dest1, dest2] in self.canMove(pos1, pos2, state, flipped):
            return True
        else:
            return False


    def canMove(self, pos1, pos2, state, flipped):
        # pos1 and pos2 are the position of the piece that is currently being investigated
        moves = []

        cont1 = True
        cont2 = True
        cont3 = True
        cont4 = True
        for r in range(1,8):
            if cont1 == True and pos1 + r in range(0,8) and pos2 in range(0,8):
                if state[pos1 + r, pos2] != 0:
                    cont1 = False
                moves.append([pos1 + r, pos2])

            if cont2 == True and pos1 - r in range(0,8) and pos2 in range(0,8):
                if state[pos1 - r, pos2] != 0:
                    cont2 = False
                moves.append([pos1 - r, pos2])

            if cont3 == True and pos1 in range(0,8) and pos2 - r in range(0,8):
                if state[pos1, pos2 - r] != 0:
                    cont3 = False
                moves.append([pos1, pos2 - r])

            if cont4 == True and pos1 in range(0,8) and pos2 + r in range(0,8):
                if state[pos1, pos2 + r] != 0:
                    cont4 = False
                moves.append([pos1, pos2 + r])


        return moves