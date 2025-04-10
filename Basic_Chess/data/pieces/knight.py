class knight:
    def __init__(self, pos1, pos2, colour, name):
        self.pos1 = pos1
        self.pos2 = pos2
        self.colour = colour
        self.name = name

        if colour == 'white':
             self.key = 2
        else: self.key = 8

    def check(self, dest1, dest2, pos1, pos2, state, flipped):
        if dest1 in range(8) and dest2 in range(8) and [dest1, dest2] in self.canMove(pos1, pos2, state, flipped):
            return True
        else:
            return False


    def canMove(self, pos1, pos2, state, flipped):
        # pos1 and pos2 are the position of the piece that is currently being investigated
        moves = []

        for r in [-1, 1]:
            if pos1 + 2 in range(0,8) and pos2 + r in range(0,8):
                moves.append([pos1 + 2, pos2 + r])

            if pos1 - 2 in range(0,8) and pos2 + r in range(0,8):
                moves.append([pos1 - 2, pos2 + r])

            if pos1 + r in range(0,8) and pos2 + 2 in range(0,8):
                moves.append([pos1 + r, pos2 + 2])

            if pos1 + r in range(0,8) and pos2 - 2 in range(0,8):
                moves.append([pos1 + r, pos2 - 2])


        return moves
    