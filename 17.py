a = float(input())
while True:
    if a < 2:
        break
    else:
        a = a ** 0.5
        print(f'{a:.3f}')
