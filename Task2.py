# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

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

# Для определения длины результирующего списка, использовал "костыль" в виде + 0.5, 
# чтобы не подключать библиотеку math  

def Get_Mult(my_list):
    new_list = []
    range_list = int(len(my_list)/2 + 0.5) 
    for i in range(range_list):
        new_list.append(my_list[i] * my_list[-i-1])
    return new_list    

my_list = Get_List()
print()
print (f'Исходный список: {my_list}')
print()

new_list = Get_Mult(my_list)
print(f'Произведение пар чисел исходного списка: {new_list}')
print()