from personagem import Personagem

class Heroi(Personagem):
    """
    A classe Heroi representa um personagem herói que herda de Personagem.
    Adiciona atributos como poder e nível, além de métodos exclusivos.
    """
    def __init__(self, nome, idade, vida, poder, nivel=1):
        super().__init__(nome, idade, vida)
        self.poder = poder
        self.nivel = nivel

    def atacar(self, inimigo):
        """
        Realiza um ataque em outro personagem, reduzindo sua vida.
        """
        if isinstance(inimigo, Personagem):
            dano = 10 * self.nivel
            inimigo.vida = max(0, inimigo.vida - dano)
            print(f'{self.nome} atacou {inimigo.nome} causando {dano} de dano!')
        else:
            print("O alvo não é um personagem válido.")

    def subir_nivel(self):
        """
        Aumenta o nível do herói e também sua vida.
        """
        self.nivel += 1
        self.upgrade_vida(20)
        print(f'{self.nome} subiu para o nível {self.nivel}!')

    def salvar_refem(self):
        """
        Simula o herói salvando um refém.
        """
        print(f"{self.nome} salvou um refém inocente! 🛡️")

    def usar_pocao(self):
        """
        Recupera a vida do herói usando uma poção.
        """
        print(f"{self.nome} usou uma poção de cura! ❤️")
        self.upgrade_vida(30)

    def __str__(self):
        return (f'Herói: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, '
                f'Poder: {self.poder}, Nível: {self.nivel}')
