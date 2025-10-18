#indice

class Opcoes:

    @staticmethod
    def opcao():
        while True:
            try:
                local = int(input("\nDigite qual opção você deseja ultilizar: "))
                return local
            except ValueError:
                print("\nErro, Digite apenas números.")
    
    @staticmethod
    def indice():
        while True:
            try:
                indiceTesks = int(input("\nDigite o índice do contato que deseja selecionar: "))
                return indiceTesks - 1
            except ValueError:
                print("\nErro, digite apenas números.")