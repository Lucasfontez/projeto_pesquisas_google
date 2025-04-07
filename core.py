import sys
from googlesearch import search
import os

def ler_termos(arquivo_entrada):
    try:
        with open(arquivo_entrada, 'r', encoding='utf-8') as file:
            termos = [linha.strip("- ").strip() for linha in file if linha.strip()]
        return termos
    except FileNotFoundError:
        print(f"Arquivo '{arquivo_entrada}' não encontrado.")
        sys.exit(1)

def buscar_links(termo, quantidade=10):
    try:
        resultados = search(termo, num_results=quantidade, lang="pt")
        return resultados
    except Exception as e:
        print(f"Erro ao buscar '{termo}': {e}")
        return []

def salvar_primeira_execucao(termos_links, caminho_saida):
    with open(caminho_saida, 'w', encoding='utf-8') as f:
        for termo, links in termos_links.items():
            for link in links:
                f.write(f"{termo} | {link}\n")
    print(f"\n Resultados salvos em: {caminho_saida}")

def main():
    if len(sys.argv) < 2:
        print("Uso: python core.py <arquivo_entrada> [quantidade_links]")
        sys.exit(1)

    arquivo_entrada = sys.argv[1]
    quantidade = int(sys.argv[2]) if len(sys.argv) > 2 else 10

    termos = ler_termos(arquivo_entrada)
    termos_links = {}

    print("Buscando links no Google...\n")
    for termo in termos:
        print(f"→ {termo}")
        links = buscar_links(termo, quantidade)
        termos_links[termo] = links

    os.makedirs("outputs", exist_ok=True)
    salvar_primeira_execucao(termos_links, "outputs/saida_1.txt")

if __name__ == "__main__":
    main()