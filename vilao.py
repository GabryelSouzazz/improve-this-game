from personagem import Personagem  # Importa a classe Personagem

class Vilao(Personagem):
    """
    A classe Vilao representa as características de um vilão no jogo.
    Herda da classe Personagem.
    """
    def __init__(self, nome, idade, vida, maldade, nivel=1):
        super().__init__(nome, idade, vida)
        niveis_validos = ['Baixa', 'Média', 'Alta']
        if maldade not in niveis_validos:
            raise ValueError(f"Nível de maldade inválido! Escolha entre {niveis_validos}")
        self.maldade = maldade
        self.nivel = nivel

    def atacar(self, personagem):
        """
        Reduz a vida de outro personagem com base no nível do vilão e na maldade.
        """
        print(f'{self.nome} atacou {personagem.nome} com maldade {self.maldade}!')
        dano_base = 10 * self.nivel

        # Multiplicador baseado no nível de maldade
        if self.maldade == 'Média':
            dano_base *= 1.5
        elif self.maldade == 'Alta':
            dano_base *= 2

        personagem.vida = max(0, personagem.vida - int(dano_base))
        print(f'{personagem.nome} perdeu {int(dano_base)} de vida! Vida atual: {personagem.vida}')

    def subir_nivel(self):
        """
        Aumenta o nível do vilão e sua vida.
        """
        self.nivel += 1
        self.upgrade_vida(15)
        print(f'{self.nome} subiu para o nível {self.nivel}!')

    def aumentar_maldade(self):
        """
        Aumenta o nível de maldade, se possível.
        """
        ordem = ['Baixa', 'Média', 'Alta']
        if self.maldade != 'Alta':
            atual_idx = ordem.index(self.maldade)
            self.maldade = ordem[atual_idx + 1]
            print(f'{self.nome} aumentou sua maldade para {self.maldade}!')
        else:
            print(f'{self.nome} já está no nível máximo de maldade!')

    def __str__(self):
        return (f'Vilão: {self.nome}, Idade: {self.idade}, Vida: {self.vida}, '
                f'Maldade: {self.maldade}, Nível: {self.nivel}')

