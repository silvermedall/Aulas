print("|| My Menu")
print("|| 1. Verificar Par")
print("|| 2. Verificar Impar")
print("|| 3. Sair")
print(" ")

n = input("||Escolha uma opção: ")

while n != "3":
    if n == "1":
        x = int(input("Introduz um número: "))
        print("O resultado é:", x % 2 == 0)
    elif n == "2":
        x = int(input("Introduz um número: "))
        print("O resultado é:", x % 2 != 0)
    else:
        print("Opção não disponivel")
