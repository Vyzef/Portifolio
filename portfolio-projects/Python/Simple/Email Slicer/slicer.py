import random
from time import sleep

def slice():
    print("Obrigado por escolher nosso programa para seu uso.") #strip remove os espaços antes e depois
    email = "ol.sa.gabriel@gmail.com"
    if email[:email.index("@") +1] != "gmail.com":
        normalUser = email[:email.index("@")]                                                                   
        normalDomain = email[email.index("@") +1]
        print("Seu nome de usuário recomendado seria...")
        sleep(1)
        print(normalUser + str(random.randint(1,99)))
        sleep(2)
        print("Seu domínio recomendado seria...")
        print(normalDomain + ".com.br")
        input("Obrigado por usar nossos serviços. Finalizando... Precione Enter para fechar.")
    else:
       gmailUser = email[:email.index("@")]
       gmailDomain = email[email.index("@")]
       print("Seu nome de usuário recomendado seria...")
       sleep(1)
       print(gmailUser + str(random.randint(1,99)))
       sleep(2)
       print("Seu domínio recomendado seria...")
       print(gmailDomain + ".com.br")
       input("Obrigado por usar nossos serviços. Finalizando... Precione Enter para fechar.")
    
slice()