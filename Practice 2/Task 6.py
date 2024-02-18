weight = int(input("Введите Ваш вес в фунтах: "))
height = int(input("Введите Ваш рост в дюймах: "))
bmi = (weight/(height**2))*703
bmi_rounded = round(bmi, 2)
print(bmi_rounded)
