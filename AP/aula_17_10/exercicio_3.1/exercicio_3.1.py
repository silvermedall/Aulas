import math

print(math.pow(2, 2))

a = int(input("Introduz o primeiro número: "))
b = int(input("Introduz o segundo número: "))

print(math.pow(a, b))


def myPow(x, y):
    print(x)
    print(y)
    print(x**y)


myPow(a, b)


def myPow2():
    x = int(input("Introduz o primeiro número: "))
    y = int(input("Introduz o segundo número: "))
    print(x**y)
    z = int(input("Introduz o terceiro número: "))
    print(x**y**z)


myPow2()
