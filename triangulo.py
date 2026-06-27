import numpy as np
from figura_base import FiguraBase

class Triangulo(FiguraBase):
    def __init__(self, p1: tuple, p2: tuple, p3: tuple):
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def obter_matriz_pontos(self) -> np.ndarray:
        # TODO: Adicionar o p1 no final da lista para "fechar" o triângulo
        # Exemplo: pontos = [self.p1, self.p2, self.p3, self.p1]
        
        # TODO: Retornar a transposta da matriz construída a partir da lista
        # return np.array(pontos).T 
        pass
