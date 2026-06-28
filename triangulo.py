import matplotlib.pyplot as plt

class Triangulo:

    # Recebe os 3 pontos e os armazena
    def __init__(self, A, B, C):
        self.pontos = [A, B, C]

        # Verifica se os pontos formam um triângulo
        if self.area() == 0:
            raise ValueError(
                "Os pontos informados são colineares e não formam um triângulo."
            )

    # Utilizada apenas para validar o triângulo
    def area(self):
        (x1, y1), (x2, y2), (x3, y3) = self.pontos

        return abs( x1 * (y2 - y3) +
            x2 * (y3 - y1) +
            x3 * (y1 - y2) ) / 2

    # Desenha o triângulo
    def visualizar(self):
        A, B, C = self.pontos

        xs = [A[0], B[0], C[0], A[0]]
        ys = [A[1], B[1], C[1], A[1]]

        plt.plot(xs, ys, linewidth=2)
        plt.fill(xs, ys, alpha=0.15)

        for rotulo, ponto in zip(["A", "B", "C"], self.pontos):
            plt.scatter(*ponto, zorder=5)
            plt.annotate(
                f"{rotulo} {ponto}",
                xy=ponto,
                xytext=(6, 6),
                textcoords="offset points"
            )

        plt.title("Triângulo")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.gca().set_aspect("equal")
        plt.show()

# Programa principal
print("=== Triângulo ===")
print("Digite as coordenadas no formato: x y")

try:
    x, y = map(float, input("Ponto A: ").split())
    A = (x, y)

    x, y = map(float, input("Ponto B: ").split())
    B = (x, y)

    x, y = map(float, input("Ponto C: ").split())
    C = (x, y)

    triangulo = Triangulo(A, B, C)

    print("\nTriângulo gerado com sucesso!")
    triangulo.visualizar()

except ValueError as erro:
    print(f"Erro: {erro}")
