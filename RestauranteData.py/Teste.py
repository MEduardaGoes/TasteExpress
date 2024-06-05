import os

restaurantes = ['Nivian', 'Bistro Bar', 'Hamburgueria Divisian']

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
    restaurantes.append(nome_restaurante)
    print(f'\nO restaurante {nome_restaurante} foi cadastrado com sucesso!')
    retorno_menu()
                             

def listar_restaurante():
    subtitle_menu('Certo vamos listar os restaurantes cadastrados!\n')
    for restaurante in restaurantes:
        print(f'.{restaurante}')
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
                print(f'Certo você escolheu a opção {choice_made}, Vamos ativar o seu restaurante!')
                
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
