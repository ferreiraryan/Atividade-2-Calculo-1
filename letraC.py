import numpy as np
from figura_base import FiguraBase

class LetraC(FiguraBase):
    def __init__(self, p_superior: tuple, p_inferior: tuple):
        """
        Conforme o PDF, recebe apenas 2 pontos da extremidade direita 
        e deve deduzir os outros 3 pontos à esquerda para formar o 'C'.
        """
        self.p_superior = p_superior
        self.p_inferior = p_inferior

    def obter_matriz_pontos(self) -> np.ndarray:
        # PESSOA A (Matemática e Lógica Geométrica):
        # TODO: Descobrir o comprimento x e y (distância/delta)
        # TODO: Deduzir os pontos P2, P3 e P4 que formam as costas do "C".
        # Dica: O P3 (meio) geralmente tem o Y no ponto médio entre p_superior e p_inferior
        
        # PESSOA B (Estrutura e Montagem):
        # TODO: Validar se a entrada faz sentido 
        # TODO: Organizar a ordem de plotagem correta (P1 -> P2 -> P3 -> P4 -> P5) 
        # TODO: Retornar a matriz via np.array().T
        pass
