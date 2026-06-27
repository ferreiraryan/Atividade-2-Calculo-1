import numpy as np
from figura_base import FiguraBase

class Quadrado(FiguraBase):
    def __init__(self, p_a: tuple, p_b: tuple):
        """
        Assume-se que p_a e p_b formam a base inferior do quadrado.
        """
        self.p_a = p_a
        self.p_b = p_b

    def obter_matriz_pontos(self) -> np.ndarray:
        # TODO: Deduzir o tamanho da aresta (distância entre p_a e p_b)
        # TODO: Calcular as coordenadas de p_c e p_d matematicamente 
        # TODO: Retornar a sequência [p_a, p_b, p_c, p_d, p_a] no formato np.array().T
        pass
