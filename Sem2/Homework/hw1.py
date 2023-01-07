# 1. Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Без работы с методами строк.

num = float(input('Input number: '))
sum = 0

power = len(str(num)) - 2
num *= 10 ** power

while num:
    sum += num % 10
    num //= 10

print(int(sum))

