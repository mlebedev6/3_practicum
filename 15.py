def a(x):
    if x <= 2:
        return 1

    for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return 0
    return 1

num = int(input())
l = []
for i in range(2, num + 1):
    if a(i) == 1:
        l.append(i)
print(*l)
