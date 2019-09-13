# !\usr\bin\python3
# _*_ coding:utf-8 _*_
"""
求数据中，元素和为特定值的元素对
"""


# method1  遍历所有元素组合的和是否满足要求
def count_t1(a, t):
    b = len(a)
    for i in range(b):
        for j in range(i+1, b):
            if a[i] + a[j] == t:
                print(a[i], a[j])


# method2  对于每个元素a[i]，遍历t-a[i]是否在数组中,
# 通过对数组排序，然后二分查找，从而提高程序效率。
def count_t2(a, t):
    b = len(a)
    for i in range(b):
        for j in range(i+1, b):
            if t - a[i] == a[j]:
                print(a[i], a[j])


count_t1([5, 6, 1, 4, 7, 9, 8], 10)
count_t2([5, 6, 1, 4, 7, 9, 8], 10)