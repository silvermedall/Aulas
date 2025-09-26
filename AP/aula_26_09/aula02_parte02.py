x = 100
a = (x * 2.54) / 1
b = (x * 1) / 2.54
c = (x * 100) / 2.54
print("a. ", a, "b. ", b, "c. ", c)

partida = 14
espera = 51
chegada = (partida + espera) % 24
print(chegada, "h")
