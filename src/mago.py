from .personagem import Personagem

class Mago(Personagem):
    def __init__(self, nome : str) -> None:
        super().__init__(nome)
        self.__forca : int = 4
        self.__inteligencia : int = 10
        self.__destreza: int = 5
    
    def atacar(self):
        print(f'{self._Personagem__nome} atacou com inteligência {self.__inteligencia}')
    
    def defender(self):
        print(f'{self._Personagem__nome} defendeu com destreza {self.__destreza}')
    
    def __str__(self):
        return f'Mago: {self._Personagem__nome}\nForça: {self.__forca}\nInteligência: {self.__inteligencia}\nDestreza: {self.__destreza}'