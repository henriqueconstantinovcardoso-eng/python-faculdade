filmes = [
    ["O Senhor dos Anéis", ["Elijah Wood", "Ian McKellen"], "Fantasia", 178, 2001],
    ["Matrix", ["Keanu Reeves", "Carrie-Anne Moss"], "Ficção Científica", 136, 1999],
    ["Cidade de Deus", ["Alexandre Rodrigues", "Leandro Firmino"], "Drama", 130, 2002]
]

opcao = 0
while opcao != 5:
    print("\n--- CATÁLOGO DE FILMES ---")
    print("1 - Inserir novo filme")
    print("2 - Filme(s) com menor duração")
    print("3 - Total de filmes e duração média por gênero")
    print("5 - Fim")
    opcao = int(input("Digite uma opção: "))
    
    if opcao == 1:
        titulo = input("Título do filme: ")
        # Validação de duplicidade
        existe = False
        for f in filmes:
            if f[0].lower() == titulo.lower():
                existe = True
        
        if existe:
            print("Filme já cadastrado!")
        else:
            atores = []
            ator = input("Informe o primeiro ator: ")
            atores.append(ator)
            while input("Adicionar mais ator? (s/n): ").lower() == 's':
                atores.append(input("Informe o próximo ator: "))
            
            genero = input("Gênero: ")
            duracao = int(input("Duração (em minutos): "))
            ano = int(input("Ano de lançamento: "))
            
            filmes.append([titulo, atores, genero, duracao, ano])
            print("Filme cadastrado com sucesso!")
            
    elif opcao == 2:
        if len(filmes) == 0:
            print("Nenhum filme cadastrado.")
        else:
            menor = filmes[0][3]
            for f in filmes:
                if f[3] < menor:
                    menor = f[3]
            print(f"\nFilmes com a menor duração ({menor} min):")
            for f in filmes:
                if f[3] == menor:
                    print(f"- {f[0]} ({f[2]}, {f[4]}) | Atores: {f[1]}")
                    
    elif opcao == 3:
        gen_busca = input("Informe o gênero desejado: ")
        cont = 0
        soma_duracao = 0
        for f in filmes:
            if f[2].lower() == gen_busca.lower():
                cont = cont + 1
                soma_duracao = soma_duracao + f[3]
                
        if cont > 0:
            media = soma_duracao / cont
            print(f"Gênero: {gen_busca} | Total de filmes: {cont} | Duração média: {media:.1f} minutos")
        else:
            print("Nenhum filme encontrado para este gênero.")
            
    elif opcao == 5:
        print("Saindo do catálogo...")
    else:
        print("Opção inválida.")

print("* Fim do programa *")
