sub = int(input())
c = 0
i = 1
while True:
    c = 2 ** i
    if c >= sub:
        break
    else:
        i += 1
        print(c)
