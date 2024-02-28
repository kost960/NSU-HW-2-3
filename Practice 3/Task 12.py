att_nfl = float(input('Введите значение параметра ATT: '))
comp_nfl = float(input('Введите значение параметра COMP: '))
yds_nfl = float(input('Введите значение параметра YDS: '))
td_nfl = float(input('Введите значение параметра TD: '))
int_nfl = float(input('Введите значение параметра INT: '))
a = ((comp_nfl/att_nfl)-0.3)*5
b = ((yds_nfl/att_nfl)-3)*0.25
c = (td_nfl/att_nfl)*20
d = 2.375-((int_nfl/att_nfl)*25)
passer_rating = ((a+b+c+d)/6)*100
print(round(passer_rating))
