x = input("Introduz a posição no tabuleiro (a1): ")

col = x[0]
lin = int(x[1])

if col == "a" or col == "c" or col == "e" or col == "g":
    if lin % 2 == 0:
        print("Branco")
    else:
        print("Preto")

if col == "b" or col == "d" or col == "f" or col == "h":
    if lin % 2 == 0:
        print("Preto")
    else:
        print("Branco")
