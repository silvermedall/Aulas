import random

num = random.randint(1, 10)
usr = int(input("Introduz um número: "))

while usr != num:
    if usr < num:
        print("O número que procuras é maior")
    elif usr > num:
        print("O número que procuras é menor")
    usr = int(input("Introduz um número: "))

print("Acertou")
