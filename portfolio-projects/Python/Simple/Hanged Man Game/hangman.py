import random

def hangman():

    wordlist = {0: "batata", 1: "papibaquigrafo", 2: "animal", 3: "espada", 4: "apostila", 5: "estudo", 6: "elefante", 
                7: "real", 8: "relação", 9: "proteção"}     #   Lista de palavras com seu determinado número
    wordcount = {0: 6, 1: 14, 2: 6, 3: 6, 4: 8, 5: 6, 6: 7, 7: 4, 8: 7, 9: 8}   #   O número de letras em cada determinada palavra
    run = True
    count = 1
    print("Obrigado por jogar Forca. Adivinhe a palavra dentro de 6 tentativas.")
    # while run:
    #     keyword = (wordlist[wordnumber])
    #     choosen = random.randint(0,9)

hangman()