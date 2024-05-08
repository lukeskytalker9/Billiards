from Wall import Wall
from Pocket import Pocket

"""
This is the collection of walls
"""
class PoolTable:

    __slots__ = ['walls', 'pockets']

    def __init__(self):


        self.walls = [
            #New wall constructor is Wall(x1 , y1 , angle , length , isPolar = true)
            Wall(0 , 0 , 0.94615 , 0),
            Wall(0.94615 , 0 , 1.01799 , -0.07184),
            #Pocket Here between 1.01799 , -0.07184 AND 1.02607 , 0.00898

            Wall( 1.02607 , 0.00898 , 0.95423 , 0.08082),
            Wall( 0.95423 , 0.08082 , 0.95423 , 1.05237),
            Wall( 0.95423 , 1.05237 , 1.00426 , 1.06119),

            #Pocket Here between 1.00426 , 1.06119 AND 1.00426 , 1.17549
            #Wall( 1.00426 , 1.17549 , ),






        ]
        self.pockets = []

        self.setup()

    def setup(self):
        #Random set of walls like this
        self.walls.append(Wall(0, 0, 1000, 0))
        self.walls.append(Wall(0, 0, 1000, 1000))
        self.walls.append(Wall(0, 0, 0, 1000))
        self.walls.append(Wall(1000, 0, 1000, 1000))
        
        self.pockets.append(Pocket(0, 0, 2))

       