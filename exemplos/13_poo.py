class Cachorro:
    nome = "Sem Nome"       # Atributo
    
    def latir(self):        # Método
        print(f"[{self.nome} diz]: Woof! Woof!")

rex = Cachorro()
rex.nome = "Rex"
rex.latir()

class Usuario:
    # O método __init__ é chamado assim que fazemos: maria = Usuario("Maria", 25)
    def __init__(self, nome, idade):
        self.nome = nome  
        self.idade = idade
    
    def exibir_perfil(self):
        print(f"Usuário {self.nome}, tem {self.idade} anos.")

user1 = Usuario("Ana", 30)
user2 = Usuario("Beto", 40)

user1.exibir_perfil()
user2.exibir_perfil()
