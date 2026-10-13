v = int(input())

l = []

for i in range(1, int(v ** (1 / 3)) + 1):
    l.append(i ** 3)
print(*l)
