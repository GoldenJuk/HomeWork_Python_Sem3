# Задайте список из нескольких чисел. Напишите программу, 
# которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.
# Пример:
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def Get_List():
    my_list = []
    while True:
        try:
            n = int(input('Введите количество элементов списка: '))
            break
        except:
            print('Ошибка. Введите число')    
    while True:
        try:
            for i in range(n): 
                my_list.append(int(input(f'Введите {i+1}-й элемент списка: ')))
            return my_list    
        except:
            print('Ошибка. Введите число')
            my_list.clear()

def Get_Sum(my_list):
    res = 0
    for i in range (1, len(my_list), 2):
        res +=my_list[i]
    return res                

my_list = Get_List()
print()
print (f'Исходный список: {my_list}')

result = Get_Sum(my_list)
print()
print(f'Cумма элементов списка, стоящих на позиции с нечетным индексом = {result}')
print()