from abc import ABC, abstractmethod

class Personagem(ABC):
    def __init__(self, nome):
        # Atributo protegido
        self.__nome = nome

    @abstractmethod
    def atacar(self):
        pass

    @abstractmethod
    def defender(self):
        pass