l = [0, 1, 2, 3, 4]
l1 = [6, 7, 8, 9, 10]
ln = l + l1
print(ln)

for n in ln:
    print(n)

print(len(ln))

for n in ln:
    print(n + 1)

w = 0
while w < len(ln):
    print(ln[w] + 1)
    w += 1

sum = 0
for n in ln:
    sum = sum + n
    print(sum)
