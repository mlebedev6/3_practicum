n, k, r = map(int, input().split())
i = 1
k = k / 100 + 1
while n < r:
    n *= k
    i += 1
print(i)
