from .personagem import Personagem

class Guerreiro(Personagem):
    def __init__(self, nome : str) -> None:
        super().__init__(nome)
        self.__forca : int = 10
        self.__inteligencia : int = 2
        self.__destreza : int = 5
    
    def atacar(self):
        print(f'{self._Personagem__nome} atacou com força {self.__forca}')
    
    def defender(self):
        print(f'{self._Personagem__nome} defendeu com destreza {self.__destreza}')
    
    def __str__(self):
        return f'Guerreiro: {self._Personagem__nome}\n Força: {self.__forca}\n Inteligência: {self.__inteligencia}s\n Destreza: {self.__destreza}'