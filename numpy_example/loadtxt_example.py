import numpy as np
from datetime import datetime


def date_to_num(s):
    """
    strptime: 标准化时间格式
    data: 获取日期部分
    weekday: 将日期转换成星期几
    """
    if type(s) == bytes:
        s = s.decode("utf-8")
    return datetime.strptime(s, "%d-%m-%Y").date().weekday()

def salary_to_float(s):
    """
    根据不同的时间单位进行转化
    """
    print(s)
    if type(s) == bytes:
        s = s.decode("utf-8")
    if s[-1] == 'b':
        return float(s[:-1]) * 10 ** 9
    elif s[-1] == 'm':
        return float(s[:-1]) * 10 ** 6
    elif s[-1] == 'k':
        return float(s[:-1]) * 10 ** 3
    else:
        return float(s[:-1])

print(date_to_num("21-07-1994"))

dates, close = np.loadtxt('data.csv', delimiter=',', skiprows=1,
    usecols=(0,1), converters={0: date_to_num, 1: salary_to_float}, unpack=True)
print ("Dates = {} | close = {}".format(dates, close))
