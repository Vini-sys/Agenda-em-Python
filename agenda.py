# Função para exibir o menu principal
def menu():
    voltarMenuPrincipal = 'S'
    while voltarMenuPrincipal == 'S':
        opcao = input('''========================================================
        
        AGENDA DE CONTATOS

        MENU:
        
        [1] - ADICIONAR CONTATO
        [2] - VER LISTA DE CONTATOS
        [3] - EXCLUIR CONTATO
        [4] - PESQUISAR CONTATO PELO NOME
        [5] - SAIR

    ========================================================
        
    ESCOLHA UMA DAS OPÇÕES ACIMA:  ''')

        if opcao =='1':
            adicionarContato()
        
        elif opcao == '2':
            verLista()
        
        elif opcao == '3':
            excluirContato()
        
        elif opcao == '4':

            pequisarNome()

        elif opcao == '5':
            exit()
        else:
            print('informe um valor válido')
        voltarMenuPrincipal = input('Deseja voltar ao menu principal: (s/n): ').upper()[0]

def main_function():
    menu()

def adicionarContato():
    # Abre o arquivo para leitura e verifica quantas linhas já existem
    with open('agenda.txt', 'r') as agenda:
        numero_contatos = len(agenda.readlines())

    # Incrementa o número para obter o próximo ID
    novo_id = numero_contatos + 1
    nome = input('Informe o nome: ')
    telefone = input('Informe o número de telefone: ')
    email = input('Informe email: ')
    agenda = open('agenda.txt','a')
    dados = f'{novo_id}; {nome.upper().strip()}; {telefone}; {email};\n'
    agenda.write(dados)
    print('CONTATO GRAVADO COM SUCESSO')

def verLista():
    #ver lista de contados adcionados
    agenda = open("agenda.txt")
    for contato in agenda:
        print()
        print(contato)
    agenda.close()

def excluirContato():
    #excluir contato
    contatoDel = input('Qual contato deseja deletar? ').upper()
    agenda = open('agenda.txt','r')
    aux1 = []
    aux2 = []
    contatoEncontrado = False
    
    for i in agenda:
        aux1.append(i)
    for i in range(0, len(aux1)):
        if contatoDel not in aux1[i]:
            aux2.append(aux1[i])
        else:
            contatoEncontrado = True

    agenda = open('agenda.txt','w')
    for i in aux2:
        agenda.write(i)
    
    if contatoEncontrado:
        print(f'contato deletado com sucesso.')
    else:
        print('contato não foi encontrado.')
    verLista()

def pequisarNome():
  
    busca_nome = input('Contato que deseja ver: ')
    agenda = open("agenda.txt",'r')
    
    contato_encontrado = False

    for contato in agenda:
        if busca_nome.upper().strip() in contato.split(";")[1].upper().strip():
            print()
            print(contato)
            contato_encontrado = True

    if not contato_encontrado:
        print()
        print('CONTATO NÃO ENCONTRADO')
    
    
        
    agenda.close()

    
# Chama a função principal
main_function()