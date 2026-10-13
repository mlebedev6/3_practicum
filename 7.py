ans = int(input())

while True:
    if ans % 2 == 0 and ans != 1:
        ans //= 2
    if ans == 1:
        print('верно')
        break
    if ans % 2 != 0:
        print('не верно')
        break
