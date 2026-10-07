agenda = []

opcao = 0
while opcao != 6:
    print("\n--- MENU AGENDA ---")
    print("1- Incluir contato e telefone")
    print("2- Consultar telefones de um contato")
    print("3- Listar todos os contatos")
    print("6- FIM")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        nome = input("Informe o nome do contato: ")
        encontrado = False
        # Verifica se o contato já existe
        for i in range(0, len(agenda), 2):
            if agenda[i] == nome:
                encontrado = True
        
        if encontrado:
            print("Erro: Contato já cadastrado!")
        else:
            telefones = []
            tel = input("Informe o primeiro telefone obrigatório: ")
            telefones.append(tel)
            
            continuar = input("Deseja adicionar mais telefones? (s/n): ")
            while continuar.lower() == 's':
                tel_extra = input("Informe o próximo telefone: ")
                telefones.append(tel_extra)
                continuar = input("Adicionar outro telefone? (s/n): ")
                
            agenda.append(nome)
            agenda.append(telefones)
            print("Contato cadastrado com sucesso!")
            
    elif opcao == 2:
        nome_busca = input("Digite o nome do contato para consulta: ")
        encontrado = False
        for i in range(0, len(agenda), 2):
            if agenda[i] == nome_busca:
                print(f"Contatos de {agenda[i]}: {agenda[i+1]}")
                encontrado = True
        if not encontrado:
            print("Contato não encontrado.")
            
    elif opcao == 3:
        print("\n--- LISTA GERAL DE CONTATOS ---")
        if len(agenda) == 0:
            print("Agenda vazia.")
        else:
            for i in range(0, len(agenda), 2):
                print(f"Nome: {agenda[i]} | Telefones: {agenda[i+1]}")
                
    elif opcao == 6:
        print("Finalizando o sistema de agenda...")
    else:
        print("Opção inválida, tente novamente.")

print("* Fim da execução *")
