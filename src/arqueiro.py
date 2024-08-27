from .personagem import Personagem

class Arqueiro(Personagem):
    def __init__(self, nome : str) -> None:
        super().__init__(nome)
        self.__forca : int = 3
        self.__inteligencia : int = 5
        self.__destreza : int = 10
    
    def atacar(self):
        print(f'{self._Personagem__nome} atacou com destreza {self.__destreza}')
    
    def defender(self):
        print(f'{self._Personagem__nome} defendeu com inteligência {self.__inteligencia}')
    
    def __str__(self):
        return f'Arqueiro: {self._Personagem__nome}\nForça: {self.__forca}\nInteligência: {self.__inteligencia}\nDestreza: {self.__destreza}'