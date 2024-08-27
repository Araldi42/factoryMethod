from src.criarPersonagem import novoPersonagem

newPersonagem = novoPersonagem()

personagem = newPersonagem.criarPersonagem('Gandalf', 'Mago')
personagem.atacar()
personagem.defender()

personagem = newPersonagem.criarPersonagem('Legolas', 'Arqueiro')
personagem.atacar()
personagem.defender()

personagem = newPersonagem.criarPersonagem('Aragorn', 'Guerreiro')
personagem.atacar()
personagem.defender()

