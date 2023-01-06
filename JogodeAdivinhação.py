import random

while True:
    
    maquina = random.randint(1,10)
    try:
        usuario = int(input("Digite um número de 1 a 10:\n"))
        if(usuario<1 or usuario>10):
            print("Erro!!! Você não digitou um número de 1 a 10!!!")
    except Exception as erro:
        maquina = 0
        print("Erro!!!")
    if(maquina != 0 and usuario>=1 and usuario<=10):
        if(maquina == usuario):
            print("\nVocê ganhou o jogo você digitou o número {} e a maquina também\nParabéns!!!".format(usuario,maquina))
        else:
            print("\nVocê perdeu você digitou o número {} e a máquina digitou o número {}\nQue pena!!!".format(usuario,maquina))

        print("\nQuer continuar jogando?\n1 - Sim\n2 - Não")
        resposta = int(input("\n"))
        if(resposta == 1):
            continue
        elif(resposta == 2):
            break
    
