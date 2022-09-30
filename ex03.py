# Задайте список (словарь не нужно выводить!) из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.
import math

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res = round((1+(1/i))**i,2)
    return res

n = int(input('Введите число: '))
a = [factorial(i) for i in range(1,n+1)]

print(a)

sum = 0

for i in range(len(a)):
    sum += a[i]
    i+=1

print("Сумма:", sum)
