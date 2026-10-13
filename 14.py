while True:
    a = input('Введите число:')
    if a.isdigit():
        print('Введено целое число:', a)
        break
    else:
        print('Ошибка. Попробуйте ещё раз.')
