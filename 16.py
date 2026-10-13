def a(n):
    l = []
    for i in range(1, n):
        if n % i == 0:
            l.append(i)
    if sum(l) == n:
        return 1
    else:
        return 0

num = int(input())

for i in range(1, num + 1):
    if a(i) == 1:
        print(i)
