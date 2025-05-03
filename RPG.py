import random

# Classe base para qualquer personagem
class Personagem:
    def __init__(self, nome, vida, ataque):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque

    def atacar(self, outro):
        dano = random.randint(1, self.ataque)
        print(f"{self.nome} atacou {outro.nome} causando {dano} de dano!")
        outro.vida -= dano

    def esta_vivo(self):
        return self.vida > 0

# Jogador controlado
class Jogador(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=100, ataque=20)
        self.pocoes = 3

    def usar_pocao(self):
        if self.pocoes > 0:
            cura = random.randint(15, 30)
            self.vida += cura
            self.pocoes -= 1
            print(f"{self.nome} usou uma poção e recuperou {cura} de vida!")
        else:
            print(f"{self.nome} não tem mais poções!")

# Inimigo do jogo
class Inimigo(Personagem):
    def __init__(self, nome):
        super().__init__(nome, vida=50, ataque=15)

# Função principal do jogo
def jogo():
    print("Bem-vindo ao RPG!")
    nome_jogador = input("Digite o nome do seu personagem: ")
    jogador = Jogador(nome_jogador)

    inimigo = Inimigo("Goblin Maligno")

    while jogador.esta_vivo() and inimigo.esta_vivo():
        print("\n--- STATUS ---")
        print(f"{jogador.nome}: {jogador.vida} de vida")
        print(f"{inimigo.nome}: {inimigo.vida} de vida")
        
        print("\n--- Ações ---")
        print("1. Atacar")
        print("2. Usar Poção")
        acao = input("Escolha sua ação: ")

        if acao == "1":
            jogador.atacar(inimigo)
        elif acao == "2":
            jogador.usar_pocao()
        else:
            print("Ação inválida!")

        if inimigo.esta_vivo():
            inimigo.atacar(jogador)

    # Resultado final
    if jogador.esta_vivo():
        print("\nVocê venceu!")
    else:
        print("\nVocê foi derrotado...")

# Rodar o jogo
if __name__ == "__main__":
    jogo()