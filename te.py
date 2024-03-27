print("*********************************")
print("Bem vindo ao jogo de adivinhação!")
print("*********************************")

numero_secreto = 42
total_de_tentativas = 3
rodada = 1

while(rodada <= total_de_tentativas):
    print("Tentativa {} de {}".format(rodada, total_de_tentativas))
    chute_str = input("Digite o seu numero: ")

    print("Voce digitou: ", chute_str)

    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if(acertou):
        print("Você acertou!")
    else:
        if(maior):
            print("Você errou! O seu chute foi maior do que o numero secreto.")
        elif(menor):
            print("Voce errou! O seu chute foi menor do que o numero secreto.")

    rodada = rodada + 1

print("Fim do Jogo!!!")