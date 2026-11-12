import random

numero_correto = random.randint(1, 10000)
tentativas = 0
maior = None
menor = None

while True:
    numero = int(input("Informe um numero: "))

    if numero < numero_correto:
        print("Numero correto é MAIOR\n")

        if (menor is None) or (menor < numero):
            menor = numero
        tentativas += 1
    elif numero > numero_correto:
        print("Numero correto é MENOR!\n")

        if (maior is None) or (maior > numero):
            maior = numero
        tentativas += 1

    else:
        print("Número encontrado!")
        tentativas += 1

        if tentativas <= 10:
            print("DESEMPENHO: Excelente!")
        elif (tentativas >= 11) and (tentativas <= 15):
            print("DESEMPENHO: Moderado!")
        else:
            print("DESEMPENHO: Ruim!")

        print(f"TENTATIVAS: {tentativas}")
        break

    print(f"MENOR: {maior}\nMAIOR: {menor}")