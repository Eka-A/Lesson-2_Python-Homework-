#  Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.

def factorial(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

n = int(input('Введите число: '))

a = [factorial(i) for i in range(1,n+1)]

print(a)
