import random

maquina = random.randint(1,10)

usuario = int(input("Digite um número de 1 a 10:\n\n"))

if(maquina == usuario):
    print("\nVocê ganhou o jogo você digitou o número {} e a maquina também\nParabéns!!!".format(usuario,maquina))
else:
    print("\nVocê perdeu você digitou o número {} e a máquina digitou o número {}\nQue pena!!!".format(usuario,maquina))

