from personagem import Personagem
from vilao import Vilao
from heroi import Heroi
from interacao import dialogar

def mostrar_personagens(heroi, vilao, npc):
    print("\n--- STATUS DOS PERSONAGENS ---")
    print(heroi)
    print(vilao)
    print(npc)

def menu(vilao_derrotado):
    print("\n===== MENU DO JOGO =====")
    print("1 - Ver personagens")
    print("2 - Dialogar (Herói vs Vilão)")
    print("3 - Lutar (Herói ataca / Vilão ataca)")
    print("4 - Evoluir (subir nível / aumentar maldade)")
    print("5 - Usar poção")
    if vilao_derrotado:
        print("6 - Salvar refém")
    print("0 - Sair")
    return input("Escolha uma opção: ")

def main():
    # Criando personagens
    heroi = Heroi('Frodo', 50, 100, poder='Ferroada', nivel=1)
    npc = Personagem('Samwise', 53, 80)
    vilao = Vilao('Sauron', 1000, 105, maldade='Baixa', nivel=1)

    vilao_derrotado = False

    print("🛡️ Bem-vindo ao jogo!")

    while True:
        opcao = menu(vilao_derrotado)

        if opcao == '1':
            mostrar_personagens(heroi, vilao, npc)

        elif opcao == '2':
            print("\n--- DIÁLOGO ---")
            dialogar(heroi, vilao)

        elif opcao == '3':
            print("\n--- COMBATE ---")
            print("1 - Atacar")
            print("2 - Fugir")
            acao = input("Escolha sua ação: ")

            if acao == '1':
                heroi.atacar(vilao)
                if vilao.vida <= 0:
                    print(f"\n🏆 {vilao.nome} foi derrotado! Vitória de {heroi.nome}!\n")
                    vilao_derrotado = True
                else:
                    vilao.atacar(heroi)
                    if heroi.vida <= 0:
                        print(f"\n💀 {heroi.nome} foi derrotado... Game Over.\n")
                        break
            elif acao == '2':
                print(f"{heroi.nome} fugiu da batalha! 🏃‍♂️")
            else:
                print("❌ Ação inválida.")

        elif opcao == '4':
            print("\n--- EVOLUÇÃO ---")
            heroi.subir_nivel()
            if not vilao_derrotado:
                vilao.subir_nivel()
                vilao.aumentar_maldade()

        elif opcao == '5':
            print("\n--- POÇÃO ---")
            heroi.usar_pocao()

        elif opcao == '6' and vilao_derrotado:
            print("\n--- MISSÃO DE RESGATE ---")
            heroi.salvar_refem()
            print(f"{npc.nome}: 'Obrigado, Sr.{heroi.nome}! Achei que nunca sairia dali vivo!'")
            print(f"{heroi.nome}: 'Está tudo bem agora. Você está seguro, {npc.nome}'")

        elif opcao == '0':
            print("\n👋 Encerrando o jogo... Até logo!")
            break

        else:
            print("❌ Opção inválida. Tente novamente.")

if __name__ == '__main__':
    main()







