# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

def list_num(n):
    list = []
    for i in range (1, n+1):
      list.append((1+1/i)**i)
    return list

def sum(list):
    sum = 0
    for i in range (len(list)):
      sum = sum + list[i]
    return sum


n = int(input('Введите число N: '))

list = list_num(n)
print(list)

result = sum(list)
print(result)
