while True:
    a = int(input('введите число'))
    b = int(a ** 0.5)
    if a == b * b:
        print('число является полным квадратом')
        break
    else:
        print('число не полный квадрат, пробуй ещё')
