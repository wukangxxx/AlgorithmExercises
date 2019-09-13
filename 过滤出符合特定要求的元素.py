# !\usr\bin\python3
# _*_ coding:utf-8 _*_
"""
从列表中，过滤出符合要求的元素
"""


def is_odd(x):
    return x % 2 == 1


a = list(range(10))
a = list(filter(is_odd, a))
print(a)