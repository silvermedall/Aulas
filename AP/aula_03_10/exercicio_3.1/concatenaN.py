s = input("Introduz uma frase: ")
n = int(input("Introduz o número de vezes: "))
sx = ""

while n > 0:
    sx += " " + s
    n = n - 1

print(sx)
