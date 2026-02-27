usrinput = ""
total = []
final = ""
with open("AP/aula_07_11/numberData.txt", "w") as data:
    while usrinput != "999":
        usrinput = input("Escreve numeros: ")
        total.append(usrinput)
    final = ",".join(total)
    data.write(final)
