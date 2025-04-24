class pessoa:

#Metodo construtor
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

 # Método especial para exibir o objeto de forma legível
    def __str__(self):
        return f"Pessoa(nome='{self.nome}', idade={self.idade})"

#Função de boas vindas inserindo a variável
    def boas_vindas(self):
        print("Seja bem vindo:", self.nome)

#Função para recusado
    def negado(self):
        print("Seu acesso foi negado!")

#Função para verificar a idade
    def maior_idade(self):
        if self.idade >= 18:
            print("Usuário é maior de idade!")
            self.boas_vindas()
        else:
            print("Usuário é menor de idade!")
            self.negado()

#Chamando o objeto e inserindo o mesmo em uma variável
dados = pessoa("Douglas", 15)
print(dados)



class Carro:
    def __init__(self, modelo, ano):
        self.modelo = modelo
        self.ano = ano
        self.velocidade = 0  # Começa parado

    def acelerar(self):
        self.velocidade += 10

    def frear(self):
        self.velocidade = max(self.velocidade - 10, 0)

    def exibir_status(self):
        print(f"{self.modelo} ({self.ano}) está a {self.velocidade} km/h")


carro1 = Carro("Civic", 2020)
carro2 = Carro("Corolla", 2022)

carro1.acelerar()
carro1.acelerar()
carro1.exibir_status()  # Civic (2020) está a 20 km/h

carro2.acelerar()
carro2.frear()
carro2.exibir_status()  # Corolla (2022) está a 0 km/h
    


class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.compras = []  # Lista para registrar valores de compras

    def adicionar_compra(self, valor):
        self.compras.append(valor)
    
    def total_gasto(self):
        return sum(self.compras)

    def exibir_dados(self):
        print(f"Cliente: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Total gasto: R${self.total_gasto():.2f}")

    def cliente_vip(self):
        if self.total_gasto() >= 1000:
            print("Cliente VIP 🏆")
        else:
            print("Cliente comum")


cliente1 = Cliente("Douglas", 25)
cliente1.adicionar_compra(150)
cliente1.adicionar_compra(300)
cliente1.adicionar_compra(700)

cliente1.exibir_dados()
cliente1.cliente_vip()