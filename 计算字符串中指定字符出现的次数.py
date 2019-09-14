# !\usr\bin\python3
# _*_ coding _*_
"""
计算字符串中，指定字符出现的次数
"""


def count_char(s, char):
    s_dict = {}
    for si in s:
        if si in s_dict:
            s_dict[si] += 1
        else:
            s_dict[si] = 1
    return s_dict[char]


count_char('abcdefgdcbaa', 'a')