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

**Entrada:** 2 pontos da abertura à direita:

- `P1`: ponto superior
- `P5`: ponto inferior

**Tarefas:**

1. Definir a largura (eixo X) a partir da altura:

```text
altura = y_superior - y_inferior
```

2. Encontrar o ponto médio da "costa" esquerda (eixo Y).

3. Deduzir os três pontos restantes:

- Canto superior esquerdo (`P2`)
- Meio esquerdo (`P3`)
- Canto inferior esquerdo (`P4`)

4. Organizar o traçado na ordem:

```text
P1 → P2 → P3 → P4 → P5
```

> Não é necessário fechar a figura retornando para `P1`.

**Saída:**

```python
return np.array(pontos).T
```

---

## 🚀 Como testar

Para validar se o módulo está funcionando, execute:

```bash
python main.py
```

Se o código estiver correto, uma janela do **Matplotlib** será aberta renderizando a figura.

Caso o script exiba um **[Aviso]**, significa que:

- a classe ainda contém `pass`; ou
- o contrato definido por `FiguraBase` foi quebrado.
