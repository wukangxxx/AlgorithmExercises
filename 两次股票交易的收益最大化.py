# !\usr\bin\python3
# _*_ coding:utf-8 _*_
"""
求得两次股票交易的最大收益
分别尝试以每个交易日进行分割，得到两个子过程；
分别求得每次分割后的子过程的最大收益，然后求和；
利用全局变量储存最大收益值。
"""

a = list(map(int, input().split()))
b = sorted(a, reverse=True)
output = 0
for k in b:
    index = a.index(k)
    a1 = a[:index+1]
    a2 = a[index+1:]
    sum = 0
    min1_p, max1_p = 99999, 0
    for i in range(len(a1)):
        min1_p = min(min1_p, a1[i])
        max1_p = max(max1_p, a1[i] - min1_p)
    sum += max1_p
    min2_p, max2_p = 99999, 0
    for j in range(len(a2)):
        min2_p = min(min2_p, a2[j])
        max2_p = max(max2_p, a2[j] - min2_p)
    sum += max2_p
    output = max(output, sum)
print(output)