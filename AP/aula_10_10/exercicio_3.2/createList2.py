l = []
usr = input("Introduz algo: ")

while usr != "fim":
    for n in l:
        if n == usr:
            l.remove(n)
    l.append(usr)
    print(l)
    usr = input("Introduz algo: ")
