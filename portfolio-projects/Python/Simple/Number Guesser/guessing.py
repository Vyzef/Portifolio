#   In this project, my goal is to create a simple game of number guessing, where the terminal will choose randomly a number
# between 1 and 100 and the player will have to guess correctly. For each wrong guess, there is a tip. Maybe a bigger or
# smaller number, or even if it is a multiple to some other number.

#   Importa o módulo random, usado para gerar o número aleatório

import random

#   Gera o número base do jogo, define variaveis

ceiling = random.randint(1, 350)
number = random.randint(1, ceiling)

count = 1
chute = 0

print("Mano, me fala um número entre 1 e {}, você tem 7 chances." .format(ceiling))

#   O jogo inteiro dentro de um loop, onde se o jogador acertar ou passar do numero de tentativas, o jogo para.

while chute != number:
    chute = int(input())
    if (chute == number):
        print("Nossa, eu real não esperava por essa. Boa mano, você conseguiu, o número que eu tava pensando era {}." .format(number))
        break
    if (count == 4):
        print("Cuidado em, pensa direito que você passou da metade das suas tentavivas...")
    if (count == 6):
        print("Ultima tentativa, usa todo esse seu cérebro ai.")
    if (count == 7):
        print("Me desculpa mano, mas você nao conseguiu adivinhar o número. Era {}. Tenta de novo e pensa melhor na próxima." .format(number))
        break
    else:
        if (chute < number):
            print("Jogou muito baixo. Tenta um número maior.")
        else:
            print("Foi lá pro alto. Tenta mais baixo.")
        count = count + 1
