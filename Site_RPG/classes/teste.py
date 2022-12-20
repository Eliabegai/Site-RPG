import random
import os


lista =[
    "paralelepipedo",
    "gramado",
    "carro",
    "ferrari",
    "motocicleta",
    "futsal",
    "otorinolaringologista",
    "espiao",
    "rambo",
    "metallica",
    "calipso",
    "chimbinha",
    "forro",
    "samba",
    "mozart",
    "bethoven",
    "maquina"
]


palavra = list(random.choice(lista))
print(palavra)

chute = list(len(palavra)*"_")

tentativas = 0
erros = 0


def erro(erros, tentativas, letras):
    if erros == 0:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||          ERROS: ", int(erros))
        print("||          LETRAS ESCOLHIDAS: " + letras)
        print("||          ")
        print("||          ")
        print("||          ")
        print("||          ")
    if erros == 1:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||   (_)    ERROS: ", int(erros))
        print("||          LETRAS ESCOLHIDAS: " + letras)
        print("||          ")
        print("||          ")
        print("||          ")
        print("||          ")
    if erros == 2:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||   (_)    ERROS: ", int(erros))
        print("||    |     LETRAS ESCOLHIDAS: " + letras)
        print("||    |     ")
        print("||          ")
        print("||          ")
        print("||          ")

    if erros == 3:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||   (_)    ERROS: ", int(erros))
        print("||    |     LETRAS ESCOLHIDAS: " + letras)
        print("||    |     ")
        print("||   /      ")
        print("||  /       ")
        print("||          ")

    if erros == 4:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||   (_)    ERROS: ", int(erros))
        print("||    |     LETRAS ESCOLHIDAS: " + letras)
        print("||    |     ")
        print("||   / \    ")
        print("||  /   \   ")
        print("||          ")

    if erros == 5:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||   (_)    ERROS: ", int(erros))
        print("||   /|     LETRAS ESCOLHIDAS: " + letras)
        print("||  / |     ")
        print("||   / \    ")
        print("||  /   \   ")
        print("||          ")

    if erros == 6:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||   (_)    ERROS: ", int(erros))
        print("||   /|\    LETRAS ESCOLHIDAS: " + letras)
        print("||  / | \   ")
        print("||   / \    ")
        print("||  /   \   ")
        print("||          ")
    
    if erros == 7:
        print("========    TENTATIVAS: ", int(tentativas))
        print("||   (_)    ERROS: ", int(erros))
        print("||   /|\    LETRAS ESCOLHIDAS: " + letras)
        print("||  / | \   GAME OVER")
        print("||   / \    ")
        print("||  /   \   ")
        print("||          ")




while erros < 7:
    a = (input("Digite uma letra: "))
    comp = len(palavra)
    
    escolhas = ""
    escolhas = escolhas + a 

    verif = list(len(palavra)*"_")

    i = 0
    for letra in palavra:
        print(letra)
        if letra == a:
            chute[i] = palavra[i]
            verif[i] = "true"
        else:
            verif[i] = "false"
        i += 1
        os.system('cls')
    
    y = 0
    for x in verif:
        if x == "false":
            y += 1

    if y == comp:
        tentativas += 1
        erros += 1
        erro(erros, tentativas, escolhas)
        print(chute)
    else:
        tentativas += 1
        erro(erros, tentativas, escolhas)
        print(chute)

    if chute == palavra:
        print("VOCÊ VENCEU")
        break