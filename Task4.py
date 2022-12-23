# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def Input_Number():
    while True:
        try:
            n = int(input('Введите целое число: '))
            return n
        except:
            print ('ОШИБКА! Введите ЦЕЛОЕ ЧИСЛО')

def Get_Convert(n):
    temp =''
    res = ''
    while n > 0:
        ost = str(n%2)
        n = n // 2
        temp += (ost)
    for i in range(len(temp)):
        res += temp[-1-i]         
    return res

n = Input_Number()
print()
res = Get_Convert(n)
print(f'Число {n} в двоичной форме: {res}')
print()