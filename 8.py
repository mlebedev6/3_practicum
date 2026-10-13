ans = int(input())

for i in range(1, ans + 1):
    if 2 ** i >= ans:
        print(i)
        break