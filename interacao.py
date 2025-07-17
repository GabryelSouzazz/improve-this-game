from heroi import Heroi
from vilao import Vilao
from personagem import Personagem

def dialogar(personagem1, personagem2):
    """
    Gera um diálogo entre um herói e um vilão (ou qualquer personagem).
    """
    print(f"\n[DIÁLOGO] {personagem1.nome} e {personagem2.nome} se encontram...\n")

    if isinstance(personagem1, Heroi) and isinstance(personagem2, Vilao):
        print(f"{personagem1.nome} (Herói): 'Eu vou impedir seus planos, {personagem2.nome}!'")
        if personagem2.maldade == 'Alta':
            print(f"{personagem2.nome} (Vilão): 'Você nunca será páreo para minha maldade suprema!'")
        else:
            print(f"{personagem2.nome} (Vilão): 'Hahaha, você acha que pode me parar?'")

    elif isinstance(personagem1, Vilao) and isinstance(personagem2, Heroi):
        print(f"{personagem1.nome} (Vilão): 'Prepare-se para cair diante da minha maldade, {personagem2.nome}!'")
        if personagem2.nivel >= 3:
            print(f"{personagem2.nome} (Herói): 'Já enfrentei piores. Não temo você!'")
        else:
            print(f"{personagem2.nome} (Herói): 'Eu... eu não vou desistir!'")

    else:
        print(f"{personagem1.nome}: 'Olá, {personagem2.nome}.'")
        print(f"{personagem2.nome}: 'Olá, {personagem1.nome}.'")

    print("\n[EVENTO] Algo está prestes a acontecer...\n")
