import numpy as np
from figura_base import FiguraBase

class LetraC(FiguraBase):
    def __init__(self, p_superior: tuple, p_inferior: tuple):
        self.p_superior = p_superior
        self.p_inferior = p_inferior

    def obter_matriz_pontos(self) -> np.ndarray:
        x_sup, y_sup = self.p_superior
        x_inf, y_inf = self.p_inferior

        altura = y_sup - y_inf
        largura = altura * 0.5  # Mantendo a proporção calculada pela equipe

        x_esq = x_sup - largura
        y_med = (y_sup + y_inf) / 2

        # Sequência exata de traçado
        pontos = [
            (x_sup, y_sup),  # P1
            (x_esq, y_sup),  # P2
            (x_esq, y_med),  # P3
            (x_esq, y_inf),  # P4
            (x_inf, y_inf)   # P5
        ]

        return np.array(pontos).T
