# Atividade 2: Construção das Figuras 📐

Este módulo é responsável por gerar as coordenadas dos objetos geométricos (**Triângulo**, **Quadrado** e **Letra C**) e visualizá-los.

A arquitetura foi desenhada para ser modular e orientada a objetos. Cada figura geométrica é uma classe isolada que assina um contrato com a classe base (`FiguraBase`), garantindo que a saída seja sempre padronizada para a engine de plotagem e, futuramente, para a multiplicação da matriz de rotação (Atividade 4).

---

## 🏗️ Arquitetura e Contrato
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
