import sympy as sym
import matplotlib.pyplot as plt
import numpy as np

x, y = sym.symbols('x y', real=True)

class iWall:
    """An implementation of a wall using implicit equations of x and y"""

    def __init__(self, eq, bound, lim, res) -> None:
        self.lim = lim
        self.res = res
        self.eq = sym.parse_expr(eq)
        self.bound = bound
        self._eval = sym.lambdify([x, y], self.eq, 'numpy')
        self._diff = sym.lambdify([x, y], sym.idiff(self.eq, x, y), 'numpy')

    def is_inside(self, point, padding=0) -> bool:
        return self._eval(point[0], point[1]) < (self.bound - padding)

    def get_slope(self, point) -> float:
        return self._diff(point[0], point[1])

    def show(self) -> None:
        X, Y = np.meshgrid(np.linspace(-self.lim, self.lim, self.res), np.linspace(-self.lim, self.lim, self.res))
        plt.gca().set_aspect('equal')
        plt.contour(X, Y, self._eval(X, Y), levels=[self.bound])

    def random_point_inside(self, padding=0):
        point = np.random.default_rng().uniform(-self.lim, self.lim, 2)
        while not self.is_inside(point, padding=padding):
          point = np.random.default_rng().uniform(-self.lim, self.lim, 2)
        return point
