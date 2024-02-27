import turtle as t

# Пропорции и параметры.
multiplier = 3
radius = 50 * multiplier
font_size = 5 * multiplier
contour_width = 2 * multiplier
start_pos = (0, -100)

# Данные для диаграммы.
stats = [350, 100, 50, 150, 350]

# Цветовое оформление.
colors = ['lightblue', 'orange', 'green', 'blue', 'red']
font_color = 'black'
contour_color = 'darkgray'

# Подготовка к началу черчения.
t.tracer(False)
t.up()
t.goto(start_pos)
t.down()
stats = [round(i * 360 / sum(stats)) for i in stats]

# Черчение диаграммы.
for i in range(len(stats)):
    t.pencolor("white")
    t.fillcolor(colors[i])
    t.begin_fill()
    t.circle(radius, stats[i])
    t.lt(90)
    t.fd(radius)
    t.lt(180 - stats[i])
    t.fd(radius)
    t.end_fill()
    t.lt(90)
    t.circle(radius, stats[i])


# Закрытие по клику.
t.exitonclick()