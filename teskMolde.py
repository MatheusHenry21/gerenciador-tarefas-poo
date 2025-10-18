#teskMolde

from abc import ABC

class Molde(ABC):
    def __init__(self, nome, materia, obs):
        self.nome = nome
        self.materia = materia
        self.obs = obs
        self.altFavorito = False

    def all_favorito(self):
        self.altFavorito = not self.altFavorito

    def __str__(self):
        materia = self.materia if self.materia != "" else "MATÉRIA NÃO INFORMADA"
        obs = self.obs if self.obs != "" else "NÃO INFORMADO"
        estrela = "⭐" if self.altFavorito == True else ""
        return f"{self.nome} -{materia}- OBS: {obs} {estrela}"