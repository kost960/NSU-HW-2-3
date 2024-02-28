import datetime


def conv_sec(seconds):
    return str(datetime.timedelta(seconds=seconds))


print(conv_sec(int(input('Введите количество секунд: '))))
