print("=== Gerador e Transposta de Matriz ===")

linhas = int(input("Informe o número de linhas (M): "))
colunas = int(input("Informe o número de colunas (N): "))

# Leitura da matriz original A
matriz_a = []
for i in range(linhas):
    linha = []
    for j in range(colunas):
        val = int(input(f"Digite o elemento A[{i}][{j}]: "))
        linha.append(val)
    matriz_a.append(linha)

# Exibição da Matriz Original
print("\nMatriz Original:")
for i in range(linhas):
    for j in range(colunas):
        print(matriz_a[i][j], end="\t")
    print()

# Construção da Matriz Transposta (linhas viram colunas, logo dimensões invertidas NxM)
matriz_transposta = []
for j in range(colunas):
    linha_t = []
    for i in range(linhas):
        linha_t.append(matriz_a[i][j])
    matriz_transposta.append(linha_t)

# Exibição da Matriz Transposta
print("\nMatriz Transposta:")
for i in range(colunas):
    for j in range(linhas):
        print(matriz_transposta[i][j], end="\t")
    print()

print("* Fim da execução matricial *")
