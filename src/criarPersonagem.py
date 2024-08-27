from .guerreiro import Guerreiro
from .mago import Mago
from .arqueiro import Arqueiro

class novoPersonagem():
    Personagem = None
    
    def criarPersonagem(self, nome, tipo):
        if tipo == 'Guerreiro':
            self.Personagem = Guerreiro(nome)
        elif tipo == 'Mago':
            self.Personagem = Mago(nome)
        elif tipo == 'Arqueiro':
            self.Personagem = Arqueiro(nome)
        else:
            print('Personagem não encontrado')
            raise ValueError
        
        print(f'\n{self.Personagem} criado com sucesso!')
        print('-----------------------------------')

        return self.Personagem    
    