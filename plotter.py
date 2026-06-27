import matplotlib.pyplot as plt
from figura_base import FiguraBase


class Plotter:
    @staticmethod
    def exibir(figura: FiguraBase, titulo: str = "Visualização geométrica"):

        matriz = figura.obter_matriz_pontos()
        
        x, y = matriz[0, :], matriz[1, :]

        plt.figure(figsize=(7, 7))
        
        plt.plot(x, y, marker='o', linestyle='-', color='#0055ff', linewidth=2, markersize=6)
        
        plt.title(titulo)
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.grid(True, linestyle='--', alpha=0.5)
        
        plt.axis('equal') 
        
        plt.show()
