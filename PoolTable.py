from Wall import Wall
from Pocket import Pocket

import numpy as np
"""
This is the collection of walls
"""
class PoolTable:

    __slots__ = ['walls', 'pockets']

    def __init__(self):

    
        self.walls = []


        self.pockets = []

        self.setup()

    def setup(self):

        table = [

            {
                "length": 0.94615,
                "angle": 0 
            },
            {
                "length": 0.1016,
                "angle": -np.pi/4
            },
            #Pocket 1 Here Instead of this
            {
                "length": 0.1143,
                "angle": np.pi/4
            },
            ##########
            {
                "length": 0.1016,
                "angle": np.pi*(3/4)
            },
            {
                "length": 0.97155,
                "angle": np.pi/2
            },
            {
                "length": 0.0508,
                "angle": 0.174533 #10 degrees
            },
            #Pocket 2 Here Instead of this
            {
                "length": 0.1143,
                "angle": np.pi/2 #10 degrees
            },
            ####
            {
                "length": 0.0508,
                "angle": np.pi - 0.174533
            },
            {
                "length": 0.97155,
                "angle": np.pi/2
            },
            {
                "length": 0.1016,
                "angle": np.pi/4
            },
            #Pocket 3 Here Instead of this
            {
                "length": 0.1143,
                "angle": np.pi*(3/4)
            },
            ###########
    

        ]
        
        currentX = 0
        currencyY = 0
        for i in range(2):
            for wall in table:

                if i == 1:
                    wall["angle"] = wall["angle"] + np.pi/2
                newX = currentX + wall["length"] * np.cos(wall["angle"])
                newY = currencyY + wall["length"] * np.sin(wall["angle"])
                self.walls.append(Wall(currentX, currencyY, newX, newY))
                currentX = newX
                currencyY = newY


       