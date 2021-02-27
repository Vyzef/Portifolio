import time

def contactList():

    list = {"Evan Van Gloss": "4445-7856", "Arthur Severo": "5419-6459", "Thiago Fritz": "9476-5488", 
    "Samuel Jonas": "7674-1846", "Erin Parker": "4876-8438"}

    print("Obrigado por usar nossos serviços. Digite 1, para verificar a lista de contatos, 2 para adicionar e 3 \n para remover um dos contatos. Digite 4 para sair.")
    time.sleep(1)
    
    run = True

    while run:
        try:
            key = int(input("Esperando Comando:"))
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
                time.sleep(1)
                print("Você deseja adicionar um contato.")
                addName = input("Por favor, digite o nome de seu contato desejado.")
                print(addName)
                time.sleep(1)
                try:
                    addNumber = int(input("Agora por favor, digite o número de seu contato."))
                except ValueError:
                    print("O valor digitado não consta como um número, tente novamente.")
                else:
                    print("O nome e número a serem adicionados são, respectivamente, {} e {}" .format(addName, addNumber))
                    addFinal = input("Está correto? Se sim, digite Sim.")
                    if addFinal == "Sim":
                        list[addName] = addNumber
                        print("Seu contato foi adicionado.")
                        time.sleep(1)
                        print("Próximo comando...")
                        continue
                    else:
                        print("Se seu numero estava incorreto, por favor, tente novamente.")
                        print("Próximo comando...")
                        continue
                continue
            if key == 3: # Por agoram deletar ainda não funciona, por conta de um erro na linha 56
                time.sleep(1)
                delete = input("Selecione de 0 a {}, este contato sera deletado." .format(len(list)))
                print(delete)
                time.sleep(2)
                confirm = (input("O contato " + list.get(delete) +  " sera deletado. Por favor, digite Sim para confirmar a remoção, e qualquer outra coisa para abortar."))
                print(confirm)
                if confirm == "Sim":
                    del list[list.get(delete)]
                    print("O contato desejado sera deletado...")
                    time.sleep(2)
                    print("Contato deletado.")
                    print("Próximo comando...")
                    continue
                else: 
                    print("O processo foi abortado. Por favor, insira a proxima ação.")
                    print("Próximo comando...")
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
    input("Aperte Enter para sair.")

contactList()
exit()