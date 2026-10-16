# 13. Programação Orientada a Objetos

Chegamos a um dos paradigmas mais importantes e revolucionários do desenvolvimento de software.

## 1. Introdução
Em vez de focar em "escrever funções que mudam variáveis" (programação procedural), a Programação Orientada a Objetos (OOP) modela o software em torno de "Objetos" que possuem tanto características (dados) quanto comportamentos (funções).

## 2. OOPs
OOP (Object-Oriented Programming) torna o código muito mais modular, seguro e fácil de entender. É o padrão da indústria para aplicações grandes, como jogos, interfaces gráficas e sistemas corporativos.

## 3. Princípios de OOP
A OOP baseia-se em 4 pilares mágicos:
1. **Encapsulamento:** Esconder o funcionamento interno de um objeto e expor apenas botões/interfaces para o mundo externo usar.
2. **Abstração:** Ocultar a complexidade bruta e lidar com o objeto num nível alto.
3. **Herança:** Criar novas classes baseadas em classes existentes (Ex: O objeto `Cachorro` herda propriedades do objeto `Animal`).
4. **Polimorfismo:** A habilidade de usar uma mesma função de formas diferentes para objetos diferentes.

## 4. Classes e Objetos
- **Classe (Class):** É a "planta baixa" ou a "forma de bolo". É onde definimos como o objeto deve ser.
- **Objeto (Object/Instância):** É a casa pronta ou o bolo assado. Você pode criar infinitos objetos a partir de uma única classe.

```python
# Criando a planta baixa (Classe)
class Carro:
    pass

# Criando um objeto de fato
meu_fusca = Carro()
```

## 5. Trabalhando com Classes e Objetos
Dentro de uma classe, nós definimos Variáveis (aqui chamadas de *Atributos*) e Funções (aqui chamadas de *Métodos*).

```python
class Cachorro:
    nome = "Sem Nome"       # Atributo
    
    def latir(self):        # Método
        print("Woof! Woof!")

rex = Cachorro()
rex.nome = "Rex"
rex.latir()
```

## 6. Construtor e Auto (Self)
Notou a palavra `self` no código acima? Como podemos criar múltiplos objetos da mesma classe (Rex, Bob, Totó), a palavra `self` aponta exatamente para "mim mesmo", a instância que está sendo manipulada no momento.

O **Construtor** (em Python, é a função `__init__`) é o primeiro método a rodar assim que um objeto nasce. Ele é perfeito para dar as configurações iniciais.

```python
class Usuario:
    # O método __init__ é chamado assim que fazemos: maria = Usuario("Maria", 25)
    def __init__(self, nome, idade):
        self.nome = nome  # O meu próprio nome recebe o nome que veio por parâmetro
        self.idade = idade
    
    def exibir_perfil(self):
        print(f"Usuário {self.nome}, tem {self.idade} anos.")

user1 = Usuario("Ana", 30)
user2 = Usuario("Beto", 40)

user1.exibir_perfil()
```

---
*Próximo Módulo:* [[14. Multithreading|14_Multithreading]]
