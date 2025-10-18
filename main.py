#main

import gerenciador, indice
from os import system
system('cls')


class Main:
    @staticmethod
    def menu():

        modificador = gerenciador.Alterador()

        while True:
            print("\n  ---MENU---")
            print("1 - Adicionar tarefa")
            print("2 - Listar tarefa")
            print("3 - Remover tarefa")
            print("4 - Favoritar")
            print("5 - Sair")

            opcao = indice.Opcoes.opcao()

            if opcao == 5:
                print("\nSaindo... até logo")
                break

            elif opcao == 1:
                modificador.add_tarefa()

            elif opcao == 2:
                modificador.listar_tarefa()

            elif opcao == 3:
                modificador.remover_tarefa()

            elif opcao == 4:
                modificador.favoritar()
                
            else:
                print("\nErro. Opção inválida, tente novamente.")

    menu()   