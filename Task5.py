# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] Негафибоначчи

def Input_Number():
	while True:
		try:
			n = int(input('Введите целое число: '))
			return n
		except:
			print ('Ошибка. Введите ЦЕЛОЕ ЧИСЛО')

def Fibo(n):
    if n == 1 or n == 2:
        return 1
    else:
        return Fibo(n-2) + Fibo(n-1)

def Fibo_Neg(n):
    if n == 0:
        return 0
    elif n == -1:
        return 1    
    else:
        return Fibo_Neg(n + 2) - Fibo_Neg(n + 1)

n = Input_Number()

nego_fibo_list = []
n *= -1
for i in range(n,0,1):
    nego_fibo_list.append(Fibo_Neg(i))
nego_fibo_list.append(0)
 
n *= -1
for i in range(1,n+1):
    nego_fibo_list.append(Fibo(i))
print()
print (f'Негафибоначчи числа {n}: {nego_fibo_list}')
print()