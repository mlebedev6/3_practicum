l = []
while True:
    a = int(input())
    if a == -1:
        break
    else:
        l.append(a)
a = 0
for i in range(len(l)):
    if a < l[i]:
        a = l[i]
print(a)
