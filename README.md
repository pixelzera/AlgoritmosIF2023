#CRUD DE JURANDY SISTEMA FINAL DE ALGORITMOS IFPAR 2023 
    #FUNÇÃO MENU
    #FUNÇÃO CADASTRO
    #FUNÇÃO LISTAR
    #FUNÇÃO EXCLUIR

    CREATE,READ,UPDATE,DELETE.

    #AQUI ESTÁ UM RASCUNHO DO ARQUIVO SEM O MENU.

  #
  clientes = []
n_clientes = 1

def menu():
    option = int(input('''
# Insira o menu aqui
'''))
    
    return option

def cadastra_cliente() :
    cliente_nome = input('Digite o nome do cliente: ')
    cliente_cep = input('Digite o cep do cliente: ')
    cliente_telefone = input('Digite o telefone do cliente: ')
    clientes_dados = (cliente_nome,cliente_cep,cliente_telefone)
    clientes.append(clientes_dados)
    print('Cliente adicionado com sucesso!!')

def mostrar_cliente() :
    for cliente in clientes:
      print(f'''
      Nome: {cliente[0]}
      Cep: {cliente[1]}
      Telefone: {cliente[2]}''')

def editar_cliente() :
    nome = input("Digite o nome do cliente que deseja editar: ")
    for i, cliente in enumerate(clientes):
        if cliente[0] == nome:
            novo_nome = input("Digite o novo nome: ")
            novo_cep = input("Digite o novo CEP: ")
            novo_telefone = input("Digite o novo telefone: ")
            clientes[i] = (novo_nome, novo_cep, novo_telefone)
            print("Informações do cliente atualizadas com sucesso.")
            break
    else:
        print("Cliente não encontrado.")

def excluir_cliente() :
    nome = input("Digite qual cliente você quer excluir: ")
    for i, cliente in enumerate(clientes):
        if cliente[0] == nome:
            clientes.pop(i)
            print("Cliente excluído com sucesso.")
            break
    else:
        print("Cliente não encontrado.")                               


def programa() :

    while True:
        option = menu()

        if option == 1 :
            cadastra_cliente()
        if option == 2 :
            mostrar_cliente()
        if option == 3 :
          editar_cliente()
        if option == 4 :
          excluir_cliente()
        if option == 5 :
          exit()
          break

programa()
