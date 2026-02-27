usrinput = input("Escreve algo: ")
usrinput2 = input("Escreve mais algo: ")
data = open("AP/aula_07_11/newData.txt", "w")
data.write(usrinput)
data.close()


def annexSentence():
    data = open("AP/aula_07_11/newData.txt", "a")
    data.write("\n" + usrinput2)
    data.close()


annexSentence()
