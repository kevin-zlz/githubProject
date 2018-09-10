import re
import time
from datetime import datetime
# rex = '12+3.5'
# # rex = 'print("hello world")'
# # eval(rex)

# f = 3.1485
# f_f = float('%5.3f' % f)
# print(f_f) # 输出结果3.15，保留小数两位

# f_2 = round(f, 3)
# print(f_2)

# s='www.baidu.com'
# s.split('.')
# print(s.split('.'))


li=[1,2,3,5,6,4]
# print(sorted(li))
# print(li)
# li.sort()
# print(li)
# li.copy()
# li.clear()
# print(li)
# li1=li.copy()
# li.pop()
# print(li1)

# s1={1,5,6,7,3,2,9}
# s1.pop()
# print(s1)

# d1={'ss':'111','dd':'2222'}
# # print(d1.items())

#def add3(m, n, *args, **other):
#     print(args)
#     print(other)
#
#
# kw = {'city': 'suzhou', 'sex': 'man'}
# add3(1, 2, 3, 4, **kw)
# add3(1, 2, 3, 4)

# def person(name, age, *, city, job):
#     print(age, name, city, job)
#
#
# person('rose', 21, city='suzhou', job='chengxuyyuan')

# timeStamp = int(time.mktime(datetime.now().timetuple()))
# print(timeStamp)
# time1=datetime.now()

# date_now=datetime.strptime('2018-8-21','%Y-%m-%d')
# days=(date_now-time1).days
# seconds=(date_now-time1).seconds
# print(days)
# print(seconds)

ss='abc123'
regx=r'\d+'
rege=re.compile(regx,flags=re.I)
res=rege.findall(ss)
print(res)

