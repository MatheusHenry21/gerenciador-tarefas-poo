#gerenciador

import teskMolde
import indice
import diversos

class Alterador:

    def __init__(self):
        self.__caderno = []

    def add_tarefa(self):
        nome = diversos.Erxecoes.nome()
        materia = input("Digite o nome da matéria(Opcional): ").capitalize().strip()
        obs = input('Campo reservado para observação(Opcional): ').capitalize().strip()

        novaTarefa = teskMolde.Molde(nome, materia, obs)
        self.__caderno.append(novaTarefa)

        print(f"\nA tarefa '{nome}' foi adicionado com sucesso!")
    
    def listar_tarefa(self):
        if not self.__caderno:
            print("\nNão há tarefas nesse caderno.")

        for i, tarefas in enumerate(self.__caderno, start=1):
            vaca = []
            print(f"\n{i} - {tarefas}")
    
    def remover_tarefa(self):
        if not self.__caderno:
            print("\nNão há tarefas nesse caderno.")
            return

        self.listar_tarefa()
        indiceLocal = indice.Opcoes.indice()

        if 0 <= indiceLocal < len(self.__caderno):
            caderno = self.__caderno[indiceLocal]

            self.__caderno.pop(indiceLocal)
            print(f"\nA tarefa '{caderno.nome}' foi excluída com sucesso.")

        else:
            print("\nÍndice inválido, tente novamente.")
    
    def favoritar(self):
        if not self.__caderno:
            print("\nNão há tarefas nesse caderno.")
            return
        
        while True:
            self.listar_tarefa()
            indiceLocal = indice.Opcoes.indice()

            if 0 <= indiceLocal < len(self.__caderno):
                caderno = self.__caderno[indiceLocal]
                caderno.all_favorito()
                status = "adicionado aos" if caderno.altFavorito == True else "removido dos"
                print(f"\nA tarefa '{caderno.nome}' foi {status} favoritos")
                return
            else:
                print("\nErro, tente novamente.")