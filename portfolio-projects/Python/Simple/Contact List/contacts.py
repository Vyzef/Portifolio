import time

def contactList():

    list = {"Evan Van Gloss": "4445-7856", "Arthur Severo": "5419-6459", "Thiago Fritz": "9476-5488", 
    "Samuel Jonas": "7674-1846", "Erin Parker": "4876-8438"}

    print("Obrigado por usar nossos serviços. Digite 1, para verificar a lista de contatos, 2 para adicionar e 3 \n para remover um dos contatos. Digite 4 para sair.")
    time.sleep(1)
    
    run = True

    while run:
        try:
            key = int(input("Esperando Resposta:"))
        except ValueError:
            print("O valor digitado não consta na nossa base de dados.")
            time.sleep(1)
            print("Por favor, digite um dos números indicados.")
        else:
            if key == 1:
                print("Contatos Carregando")
                time.sleep(2)
                print(list)
                print("Próximo comando...")
                continue
            if key == 2:
                print("2")
                continue
            if key == 3:
                print("3")
                continue
            if key == 4:
                run = False
                print("Obrigado por usar nossos serviços.")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                time.sleep(1)
                print(".")
                print("Finalizando")
                break

def exit():
    print = input("Aperte Enter para sair.")

contactList()
exit()