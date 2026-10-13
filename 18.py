a = int(input())
b = 0
for i in range(1, a):
    for j in range(1, int(a ** 0.5 + 1)):
        if i ** 2 + j ** 2 == a:
            b += 1
print(b)
