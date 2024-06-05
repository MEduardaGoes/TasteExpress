import os

restaurantes = [{'nome': 'New City', 'categoria': 'Japonesa', 'ativo':False },
                {'nome': 'Jow Pizza', 'categoria': 'Italiano', 'ativo':True},
                {'nome': 'Doces Mr M', 'categoria': 'Doceria', 'ativo':False}
]

def nome_app():
    print('Ｓａｂｏｒ Ｅｘｐｒｅｓｓ\n')

def menu_opções():
    print('1. Cadastrar Restaurante')
    print('2. Listar Restaurante')
    print('3. Ativar Restaurante')
    print('4. Sair\n')

def subtitle_menu(texto):
    os.system('cls')
    print(texto)
    print()
        
def cadastro_new():
    subtitle_menu('Certo vamos realizar o cadastro do seu restaurante!\n')
    nome_restaurante = input('Digite o nome do seu restaurante: ')
    categoria_restaurante = input(f'Digite o nome da categoria do seu restaurante {nome_restaurante}: ')
    dados_restaurante = {'nome':nome_restaurante, 'categoria':categoria_restaurante, 'ativo':False}
    restaurantes.append(dados_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!')
    retorno_menu()
                             
def alterar_estado_restaurante():
    subtitle_menu('Alterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja ajustar: ')
    findrestaurante = False 
    
    for restaurante in restaurantes: 
        if nome_restaurante == restaurante['nome']:
            findrestaurante = True
            restaurante['ativo'] = not restaurante['ativo']
            msg = (f'O restaurante {nome_restaurante} foi ativado com sucesso!' 
                   if restaurante['ativo'] 
                   else f'O restaurante {nome_restaurante} foi desativado com sucesso!')
            print(msg)
    if not findrestaurante:
        print(f'O restaurante {nome_restaurante} não foi encontrado!')
        retorno_menu()
        
def listar_restaurante():
    subtitle_menu('Certo vamos listar os restaurantes cadastrados!\n')
    
    print(f"{'Nome do restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria = restaurante['categoria']
        ativo = 'ativado' if restaurante['ativo'] else 'desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}')

    retorno_menu()
                             
def choice():
    try:
        choice_made = int(input("Escolha uma opção: "))
        match choice_made: 
        
            case 1:
                cadastro_new()
                
            
            case 2:
                listar_restaurante()
            
            case 3:
                alterar_estado_restaurante()
                
            case 4:
                finalizar_app()
                print(f'Certo você escolheu a opção {choice_made}, Tchauzinho!\n')
            
            case _:
                opcão_inv()
    except ValueError:
        opcão_inv()

def retorno_menu():
    input('Digite uma tecla para retornar ao menu principal: ')
    main()
    
def opcão_inv():
    retorno_menu()
def finalizar_app():
    os.system('cls')
def main ():
    os.system('cls')
    nome_app()
    menu_opções()
    choice()

if __name__ == '__main__':
        main() 