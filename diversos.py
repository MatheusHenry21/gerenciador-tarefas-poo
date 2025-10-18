#diversos

class Erxecoes:

    @staticmethod
    def nome():
        while True:
            nome = input("\n*Digite o nome da tarefa: ").capitalize().strip()
            if nome == "":
                print("\nErro, Campo Obrigatório.")
            else: return nome
