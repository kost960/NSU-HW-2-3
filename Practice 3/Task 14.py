grad = float(input()) * 2
h = int(grad // 60)
m = int(grad % 60)
print('{}:{:02d}'.format(h, m))
