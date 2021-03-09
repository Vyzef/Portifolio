import random

randomList = sorted((random.sample(range(0, 101), 25)))
aim = int(input("Digite o número que você deseja encontrar "))
exist = False

def search(list, aim):
    global exist
    start = 0
    end = len(randomList) - 1

    while start <= end:
        midpoint = start + (end - start)//2
        midvalue = list[midpoint]

        if midvalue == aim:
            exist = True
            return midpoint
        elif aim < midvalue:
            end = midpoint - 1
        else:
            start = midpoint +1
    return None
        

def main():
    print(randomList)
    if exist:
        print("Seu item estava na posição " + search(randomList, aim))
    else:
        print("Seu item não estava na lista gerada.")
    input("Aperte enter para fechar a aplicação.")

main()