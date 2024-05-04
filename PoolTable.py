from Wall import Wall

"""
This is the collection of walls
"""
class PoolTable:

    def __init__(self):
        self.walls = []

        self.setup()

    def setup(self):
        #Random set of walls like this
        self.walls.append(Wall(0, 0, 1000, 0))
        self.walls.append(Wall(0, 0, 1000, 1000))
        self.walls.append(Wall(0, 0, 0, 1000))
        self.walls.append(Wall(1000, 0, 1000, 1000))
        

       