class king:
    def __init__(self, pos1, pos2, colour, name):
        self.pos1 = pos1
        self.pos2 = pos2
        self.colour = colour
        self.name = name

        if colour == 'white':
             self.key = 5
        else: self.key = 11

    def check(self, dest1, dest2, pos1, pos2, state, flipped):
        if dest1 in range(8) and dest2 in range(8) and [dest1, dest2] in self.canMove(pos1, pos2, state, flipped):
            return True
        else:
            return False


    def canMove(self, pos1, pos2, state, flipped):
        # pos1 and pos2 are the position of the piece that is currently being investigated
        moves = []

        for i in [-1, 1]:
            moves.append([pos1 + i, pos2])
            moves.append([pos1, pos2 + i])
            moves.append([pos1 + i, pos2 + i])
            moves.append([pos1 + i, pos2 - i])

        return moves
