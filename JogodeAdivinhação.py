import random

while True:
    
    maquina = random.randint(1,10)

    usuario = int(input("Digite um número de 1 a 10:\n\n"))

    if(maquina == usuario):
        print("\nVocê ganhou o jogo você digitou o número {} e a maquina também\nParabéns!!!".format(usuario,maquina))
    else:
        print("\nVocê perdeu você digitou o número {} e a máquina digitou o número {}\nQue pena!!!".format(usuario,maquina))

    print("\nQuer continuar jogando?\n1 - Sim\n2 - Não\n")
    resposta = int(input("\n"))
    if(resposta == 1):
        continue
    elif(resposta == 2):
        break
    
