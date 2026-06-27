from abc import ABC, abstractmethod
import numpy as np

class FiguraBase(ABC):
    """
    Interface estrita para formas geométricas.
    Garante que qualquer figura exporte os pontos num formato
    compatível com as operações de álgebra linear (rotação).
    """
    
    @abstractmethod
    def obter_matriz_pontos(self) -> np.ndarray:
        """
        Retorna uma matriz numpy 2xN.
        Linha 0: Eixo X
        Linha 1: Eixo Y
        
        O último ponto deve ser idêntico ao primeiro para fechar o polígono.
        """
        pass
