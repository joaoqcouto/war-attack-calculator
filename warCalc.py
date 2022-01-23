# WAR SIM PYTHON VER.
#
# Esse simulador ataca até não sobrarem tropas
# Diferente do simulador em C que para o ataque e assume derrota caso ataque < defesa

import random


def diceRoll():
    return random.randint(1, 6)  # rola dado


def battle(attack, defense):  # função de uma batalha individual
    if attack == 0:  # ataque falhou
        return False
    elif defense == 0:  # ataque venceu
        return True
    else:
        atkDice = [0, 0, 0]
        defDice = [0, 0, 0]
        for i in range(3):
            if i == attack:  # rola os 3 dados somente se tiver 3 ou mais peças restantes
                break
            atkDice[i] = diceRoll()
        for i in range(3):
            if i == defense:  # rola os 3 dados somente se tiver 3 ou mais peças restantes
                break
            defDice[i] = diceRoll()
        atkDice.sort(reverse=True)  # prepara os dados pra comparar
        defDice.sort(reverse=True)  # prepara os dados pra comparar

        for i in range(3):
            if atkDice[i] == 0 or defDice[i] == 0:  # se for 0 não tem comparação (não tem peça a eliminar)
                break
            if atkDice[i] <= defDice[i]:
                attack -= 1
            else:
                defense -= 1
            # attack -= 1 if (atkDice[i] <= defDice[i]) else defense -= 1 # faz a comparação, subtrai uma peça

        return battle(attack, defense)


def war(attack, defense):  # função para a estatística total em 1000 simulações
    victories = 0
    for i in range(5000):
        if battle(attack, defense): victories += 1

    return victories / 5000
