import numpy as np
import matplotlib.pyplot as plt

def letra_c(p1, p5):
    x_sup, y_sup = p1
    x_inf, y_inf = p5

    altura = y_sup - y_inf
    largura = altura * 0.5

    x_esq = x_sup - largura
    y_med = (y_sup + y_inf) / 2

    P1 = (x_sup, y_sup)
    P2 = (x_esq, y_sup)
    P3 = (x_esq, y_med)
    P4 = (x_esq, y_inf)
    P5 = (x_sup, y_inf)

    pontos = [P1, P2, P3, P4, P5]

    return np.array(pontos).T


def main():
    A = int(input("PONTO X do P1: "))
    B = int(input("PONTO Y do P1: "))
    C = int(input("PONTO X do P5: "))
    D = int(input("PONTO Y do P5: "))

    C1 = (A, B)
    C2 = (C, D)

    pontos = letra_c(C1, C2)

    x = pontos[0]
    y = pontos[1]

    plt.plot(x, y, marker='o', linestyle='-', color='blue')
    plt.title("Gráfico com pontos")
    plt.xlabel("Eixo X")
    plt.ylabel("Eixo Y")
    plt.grid(True)
    plt.axis('equal')
    plt.show()

main()
