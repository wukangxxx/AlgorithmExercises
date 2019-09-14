# !\usr\bin\python3
# _*_ coding:utf-8 _*_
"""
输入一个字符串，判断其是否为数字（整数或者小数）
"""


# 判断字符串是否为整数（含正负号），而自带str.isdigit()则不能判断含正负号的整数。
def is_int(s):
    try:
        return isinstance(int(s), int)
    except ValueError:
        return False


# 判断字符串是否为小数
def is_float(s):
    if s.count('.') == 1:
        s_l, s_r = s.split('.')
        if s_r.isdigit() and is_int(s_l):
            return True
        else:
            return False
    else:
        return False


'-2'.isdigit()  # 不能判断含有正负号的整数
is_int('-2')
is_float('-2.3')