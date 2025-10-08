a = int(input("Introduza o número do dia de inicio das férias: "))
b = int(input("Introduza a duração das férias em dias: "))
c = (a + b) % 7

if c == 0:
    print("Domingo")
elif c == 1:
    print("Segunda-feira")
elif c == 2:
    print("Terça-feira")
elif c == 3:
    print("Quarta-feira")
elif c == 4:
    print("Quinta-feira")
elif c == 5:
    print("Sexta-feira")
elif c == 6:
    print("Sábado")
