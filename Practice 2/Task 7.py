level = int(input("Введите уровень осадков в см: "))
h = level/100
s = int(input("Введите площадь выпадения осадков в кв. метрах: "))
vol_waterinm = h*s
vol_waterinl = vol_waterinm*1000
vol_waterinl_r = round(vol_waterinl)
print(vol_waterinl_r)