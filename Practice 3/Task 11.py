import math

a = int(input())
b = int(input())
c = int(input())
if a + b <= c or a + c <= b or b + c <= a:
    print('Треугольник не существует')
else:
    alpha = math.acos((b**2+c**2-a**2)/(2*b*c))
    beta = math.acos((a**2+c**2-b**2)/(2*a*c))
    gamma = math.acos((a**2+b**2-c**2)/(2*b*a))
    print(round(math.degrees(alpha)),round(math.degrees(beta)), round(math.degrees(gamma)))