# Atividade 2: Construção das Figuras 📐

Este módulo é responsável por gerar as coordenadas dos objetos geométricos (**Triângulo**, **Quadrado** e **Letra C**) e visualizá-los.

A arquitetura foi desenhada para ser modular e orientada a objetos. Cada figura geométrica é uma classe isolada que assina um contrato com a classe base (`FiguraBase`), garantindo que a saída seja sempre padronizada para a engine de plotagem e, futuramente, para a multiplicação da matriz de rotação (Atividade 4).

---

## 🏗️ Arquitetura e Contrato (Regra de Ouro)

Todas as formas devem herdar de `FiguraBase` e implementar o método `obter_matriz_pontos()`.

### Obrigações do método

- Retornar um `np.ndarray` bidimensional no formato **2 × N** (2 linhas, N colunas).
- **Linha 0:** Coordenadas X.
- **Linha 1:** Coordenadas Y.
- O último ponto da matriz deve ser igual ao primeiro para **fechar** o traçado do polígono.

Para converter uma lista de tuplas `[(x1, y1), (x2, y2), ...]` no formato exigido, utilize:

```python
return np.array(pontos).T
```

---

## ✅ O que já está feito (Infraestrutura)

### `figura_base.py`

Interface abstrata contendo o contrato que todas as figuras devem seguir.

### `grafico.py` (Plotter)

Engine de renderização utilizando `matplotlib`.

Já configura proporção **1:1** (`axis('equal')`) para evitar distorções visuais durante as rotações.

### `main.py`

Pipeline de execução e integração contínua.

Possui blocos `try/except` para permitir a execução mesmo com formas ainda não implementadas.

---

## 🛠️ O que deve ser feito (To-Dos da Equipe)

Cada integrante (ou dupla) deve escolher um dos arquivos de template gerados e substituir o `pass` pela lógica matemática correspondente.

### 1. `triangulo.py`

**Entrada:** 3 pontos (tuplas).

**Tarefas:**

1. Montar a lista sequencial com os 3 pontos.
2. Repetir o primeiro ponto no final para fechar a figura.

**Saída:**

```python
return np.array(pontos).T
```

---

### 2. `quadrado.py`

**Entrada:** 2 pontos formando a aresta inferior (`A` e `B`).

**Tarefas:**

1. Calcular a distância (aresta) entre `A` e `B`.
2. Deduzir matematicamente as coordenadas dos pontos `C` (superior direito) e `D` (superior esquerdo).
3. Montar a sequência:

```text
A → B → C → D → A
```

**Saída:**

```python
return np.array(pontos).T
```

---

### 3. `letra_c.py` (Dupla)

```
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
```
