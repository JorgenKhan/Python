## Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

print(f"{((x2 - x1) ** 2 + (y2 - y1) ** 2) **0,5}") ##вроде должно быть так по формуле
## в с# мы использовали Math.Sqrt и Math.Pow. Но результат у меня двойной)