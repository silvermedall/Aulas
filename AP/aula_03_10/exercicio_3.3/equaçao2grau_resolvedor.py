a = int(input("Introduz o primeiro número: "))
b = int(input("Introduz o segundo número: "))
c = int(input("Introduz o terceiro número: "))

res_pos = (-b + (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)
res_neg = (-b - (b**2 - 4 * a * c) ** (1 / 2)) / (2 * a)

print("Os resultados da equação de segundo grau são:", res_pos, "e", res_neg)
