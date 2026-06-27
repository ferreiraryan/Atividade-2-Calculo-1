from triangulo import Triangulo
from quadrado import Quadrado
from letraC import LetraC
from plotter import Plotter

def main():
    print("Iniciando pipeline de renderização geométrica...")

    try:
        t = Triangulo((2, 1), (6, 1), (4, 3))
        Plotter.exibir(t, "1. Triângulo a partir de 3 pontos")
        print("Triângulo renderizado.")
    except Exception as e:
        print(f"Falha ao renderizar Triângulo. A equipe já implementou? Erro: {e}")

    try:
        q = Quadrado((1, 1), (5, 1))
        Plotter.exibir(q, "2. Quadrado a partir de 2 pontos")
        print("Quadrado renderizado.")
    except Exception as e:
        print(f"Falha ao renderizar Quadrado. A equipe já implementou? Erro: {e}")

    try:
        c = LetraC((5, 6), (5, 1))
        Plotter.exibir(c, "3. Letra C a partir de 2 pontos")
        print("Letra C renderizada.")
    except Exception as e:
        print(f"Falha ao renderizar Letra C. A equipe já implementou? Erro: {e}")

if __name__ == "__main__":
    main()
