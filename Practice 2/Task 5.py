a = float(input('Введите число: '))
p = float(input('Введите процент: '))
procent = a * p / 100
procent_rounded = round(procent, 2)
print(procent_rounded)