try:
    f = open('exapmle.txt')
    s = input()
    if s == 'стр':
        for i in f:
            print(str(i))
    elif s == 'цел':
        print(f.read())
except FileNotFoundError:
    print('Файл не найден')