import numpy as np
from figura_base import FiguraBase

class Quadrado(FiguraBase):
    def __init__(self, p_a: tuple, p_b: tuple):
        self.p_a = p_a
        self.p_b = p_b

    def obter_matriz_pontos(self) -> np.ndarray:
        x_a, y_a = self.p_a
        x_b, y_b = self.p_b
        
        vetor_ab_x = x_b - x_a
        vetor_ab_y = y_b - y_a
        
        # Rotaciona o vetor 90 graus (normal) para subir a aresta lateral
        vetor_normal_x = -vetor_ab_y
        vetor_normal_y = vetor_ab_x
        
        x_c = x_b + vetor_normal_x
        y_c = y_b + vetor_normal_y
        p_c = (x_c, y_c)
        
        x_d = x_a + vetor_normal_x
        y_d = y_a + vetor_normal_y
        p_d = (x_d, y_d)
        
        pontos = [self.p_a, self.p_b, p_c, p_d, self.p_a]
        return np.array(pontos).T
