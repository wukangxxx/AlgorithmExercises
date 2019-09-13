# !\usr\bin\python3
# _*_ coding:utf-8 _*_
"""
过滤字符串中的重复值
"""
L = 'AA, BB, CC, DD, ABC, AA, ABC'
L1 = L.split(', ')
L2 = [x for x in L1 if L1.count(x) == 1]
L3 = list(set(L1))
S = ','.join(L3)
print(S)