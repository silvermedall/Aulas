a = input("Frase em maiusculas: ")
b = int(input("Chave: "))


def cifrar(string: str, key):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for i in string:
        i = 0
        for j in alphabet:
            j = 0
            if string[i] != alphabet[j]:
                j += 1
            else:
                cypherString = ""
                cypherString += alphabet[j]
                print(cypherString)
                j += 1
        i += 1
        print(string)


cifrar(a, b)
