import numpy as np
from figura_base import FiguraBase

class Triangulo(FiguraBase):
    def __init__(self, p_a: tuple, p_b: tuple, p_c: tuple):
        self.p_a = p_a
        self.p_b = p_b
        self.p_c = p_c

        if self._area() == 0:
            raise ValueError("Os pontos informados são colineares e não formam um triângulo.")

    def _area(self):
        (x1, y1), (x2, y2), (x3, y3) = self.p_a, self.p_b, self.p_c
        return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2

    def obter_matriz_pontos(self) -> np.ndarray:
        pontos = [self.p_a, self.p_b, self.p_c, self.p_a]
        return np.array(pontos).T


































































