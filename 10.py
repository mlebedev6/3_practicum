l = []
while True:
    a = float(input())
    if a == 0:
        break
    else:
        l.append(a)
c = 0
for i in range(len(l) - 1):
    if l[i] > l[i + 1]:
        c += 1
print(c)
