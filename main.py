import sys
from triangulo import Triangulo
from quadrado import Quadrado
from letra_c import LetraC
from grafico import Plotter

def ler_ponto(nome: str) -> tuple:
    while True:
        try:
            print(f"Digite as coordenadas X e Y para o {nome} (separadas por espaço):")
            coords = input("-> ").strip().split()
            if len(coords) != 2:
                raise ValueError("Forneça exatamente dois valores.")
            return (float(coords[0]), float(coords[1]))
        except ValueError as e:
            print(f"[ERRO] Entrada inválida. {e} Tente novamente.\n")

def main():
    while True:
        print("\n=== Renderizador Geométrico ===")
        print("1. Triângulo (3 pontos)")
        print("2. Quadrado (2 pontos da base)")
        print("3. Letra C (2 pontos extremidade direita)")
        print("0. Sair")
        
        opcao = input("\nEscolha uma opção: ").strip()

        if opcao == '0':
            print("Saindo...")
            sys.exit(0)
            
        elif opcao == '1':
            print("\n-- Construindo Triângulo --")
            try:
                a = ler_ponto("Ponto A")
                b = ler_ponto("Ponto B")
                c = ler_ponto("Ponto C")
                fig = Triangulo(a, b, c)
                Plotter.exibir(fig, "Triângulo a partir de 3 pontos")
            except Exception as e:
                print(f"[FALHA] {e}")
                
        elif opcao == '2':
            print("\n-- Construindo Quadrado --")
            try:
                a = ler_ponto("Ponto A (Base Inferior Esquerda)")
                b = ler_ponto("Ponto B (Base Inferior Direita)")
                fig = Quadrado(a, b)
                Plotter.exibir(fig, "Quadrado a partir de 2 pontos")
            except Exception as e:
                print(f"[FALHA] {e}")
                
        elif opcao == '3':
            print("\n-- Construindo Letra C --")
            try:
                p_sup = ler_ponto("Ponto P1 (Superior Direito)")
                p_inf = ler_ponto("Ponto P5 (Inferior Direito)")
                fig = LetraC(p_sup, p_inf)
                Plotter.exibir(fig, "Letra C a partir de 2 pontos")
            except Exception as e:
                print(f"[FALHA] {e}")
                
        else:
            print("[ERRO] Opção inválida. Escolha entre 0 e 3.")

if __name__ == "__main__":
    main()
