data = open("AP/aula_07_11/numberData.txt", "r")
string = data.readline()
data.close()
separator = ","
list1 = string.split(separator)
list2 = []
for i in list1:
    list2.append(int(i))
print("1: ", list2)

list3 = []
for i in list2:
    if i >= 20:
        list3.append(i)
print("2: ", list3)
