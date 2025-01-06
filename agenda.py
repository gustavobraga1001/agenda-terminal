def adicionar_contato(contatos): 
    nome = input("Digite o nome do contato: ") 
    telefone = input("Digite o telefone do contato: ") 
    email = input("Digite o e-mail do contato: ")

    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito": False}

    contatos.append(contato)

    print(f"\nO contato do {nome} foi adicionado com sucesso!\n")
    return

def ver_contatos(contatos) :
    print("\nLista de Contatos: ")

    for indice, contato in enumerate(contatos, start=1) :
        favorito = "⭐" if contato["favorito"] else " "
        print(f"{indice}. [{favorito}] {contato['nome']}")
    
    print("\n ")

def atualizar_contatos (contatos) :
    ver_contatos(contatos)
    indice = int(input("Digite o número do contato que deseja atualizar: ")) - 1

    if indice < 0 or indice >= len(contatos):
        print("Índice inválido! Por favor, tente novamente.")
        return
    
    while True: 
        print("\nO que você deseja atualizar?")
        print("1. Editar nome")
        print("2. Editar telefone")
        print("3. Editar email")

        campo = input("Escolha uma opção (1-3): ")
        if campo == "1":
            chave = "nome"
            break
        elif campo == "2":
            chave = "telefone"
            break
        elif campo == "3":
            chave = "email"  
            break 
        
    novo_dado = input("Digite o novo valor: ") 

    contatos[indice][chave] = novo_dado
    print("\nContato atualizado com sucesso!\n")

    return

def favoritar_contato (contatos) :
    ver_contatos(contatos)
    indice = int(input("Digite o número do contato que deseja marcar/Desmarcar como favorito: ")) - 1

    status = contatos[indice]["favorito"]
    contatos[indice]["favorito"] = not status

    print("\nContato atualizado com sucesso!\n")

    return

def ver_favoritos(contatos) :
    print("\nLista de favoritos: ")

    for indice, contato in enumerate(contatos, start=1) :
        favorito = "⭐" if contato["favorito"] else " "
        if contato["favorito"] :
            print(f"{indice}. [{favorito}] {contato['nome']}")
        
    print("\n ")
    return

def excluir_contato(contatos) :
    ver_contatos(contatos)
    print("\nContato deletado com sucesso!\n")
    indice = int(input("Digite o número do contato que deseja excluir: ")) - 1

    if 0 <= indice < len(contatos):
        contatos.pop(indice)  

    else:
        print("Índice inválido!")
    return

contatos = []

while True: 
    print("Agenda de Contatos: \n")

    print("Digite a opção desejada! \n")
    
    print("1. Adicionar contato")
    print("2. Vizualizar contatos")
    print("3. Atualizar contato")
    print("4. Marcar/Desmarcar contato como favorito")
    print("5. Vizualizar contatos favoritos")
    print("6. Excluir contato")

    print("7. Finalizar programa")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        adicionar_contato(contatos)
    elif escolha == "2":
        ver_contatos(contatos)
    elif escolha == "3":
        atualizar_contatos(contatos)
    elif escolha == "4":
        favoritar_contato(contatos)
    elif escolha == "5":
        ver_favoritos(contatos)
    elif escolha == "6":
        excluir_contato(contatos)
    elif escolha == "7" :
        break

print('Progama Finalizado')