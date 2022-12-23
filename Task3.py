# Задайте список из вещественных чисел. Напишите программу, которая найдёт 
# разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

import math

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
                my_list.append(float(input(f'Введите {i+1}-й элемент списка: ')))
            return my_list    
        except:
            print('Ошибка. Введите число')
            my_list.clear()

#Здесь не смог придумать костыли, пришлось подключать math
 
def Get_Substraction(my_list):
    new_list = []
    for i in range(len(my_list)):
        temp = my_list[i] - math.floor(my_list[i])
        if temp != 0:
            new_list.append(temp)
    new_list.sort()
    res = round((new_list[-1] - new_list[0]),2)
    return res  

my_list = Get_List()
print()
res = Get_Substraction(my_list)
print(f'Разница между максимальным и минимальным значением дробной части элементов списка: {my_list}, отличной от 0 = {res}')
print()