# !\usr\bin\python3
# _*_ coding:utf-8 _*_
"""
检测字符串中第一个未重复的字符，并输出对应位置
时间复杂度为O(n)
"""


def first_char(s):
    n = len(s)
    char_dict = {}
    for i in range(n):
        if s[i] in char_dict:
            char_dict[s[i]] += 1
        else:
            char_dict[s[i]] = 1
    for i in range(n):
        if char_dict[s[i]] == 1:
            return s[i], i+1


if __name__ == "__main__":
    s = input('please input a string:')
    a, b = first_char(s)
    print('第一个不重复的字符为%s,出现的位置为%d'%(a, b))