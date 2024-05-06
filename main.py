from System import System
from State import State
from PoolTable import PoolTable

if __name__ == "__main__":
    initialState = State()
    walls = PoolTable()
    system = System(State(), walls)
    system.run(1000)
    pass