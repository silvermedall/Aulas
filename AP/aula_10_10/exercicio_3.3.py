myList = [11, 25, "90", "3", 56, "77", True, 1, 4, 5, 6.8]
i = 0
high = 0

print(myList)

while i < len(myList):
    if type(myList[i]) == int:
        myList[i] = myList[i] + 1
    i += 1
print(myList)

i = 0
while i < len(myList):
    if type(myList[i]) == str:
        myList[i] = int(myList[i])
    if type(myList[i]) == int:
        if myList[i] > high:
            high = myList[i]
    i += 1
print(high)

myList = [11, 25, "90", "3", 56, "77", True, 1, 4, 5, 6.8]
s = ""
i = 0
while i < len(myList):
    if type(myList[i]) == str:
        s = s + myList[i]
    i += 1
print(s)

for n in myList:
    if type(n) == bool:
        print(True)

sum = 0
i = 0
while i < len(myList):
    if type(myList[i]) == int:
        sum = sum + myList[i]
    i += 1
print(sum)

sum = 0
i = 0
while i < len(myList):
    if type(myList[i]) == str:
        myList[i] = int(myList[i])
    if type(myList[i]) == float:
        myList[i] = int(myList[i])
    if type(myList[i]) == bool:
        myList[i] = int(myList[i])
    if type(myList[i]) == int:
        sum = sum + myList[i]
    i += 1
print(sum)

myList = [11, 25, "90", "3", 56, "77", True, 1, 4, 5, 6.8]
pos = int(input("Introduz a posição: "))
val = input("Introduz algo: ")

if pos < len(myList):
    myList[pos] = val
else:
    print("Posição inválida")
print(myList)
