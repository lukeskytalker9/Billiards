from System import System
from State import State
from PoolTable import PoolTable
from Ball import Ball

if __name__ == "__main__":
    balls = [Ball(0, 0, 1, 1, 2)]
    initialState = State()
    walls = PoolTable()
    system = System(initialState, walls)
    system.run(1000)
    pass