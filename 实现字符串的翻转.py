# !\usr\bin\python3
# _*_ coding:utf-8 _*_


# 方法一：使用字符串切片操作
def method1(s):
    return s[::-1]


# 方法二：使用列表reverse方法
def method2(s):
    s_ = list(s)
    s_.reverse()
    s_r = ''.join(s_)
    return s_r


# 方法三：使用reduce方法，注意reduce(fun, seq)，首先将seq中前两个元素运用fun进行运算，
# 然后将计算结果和第三个元素进行fun运算，依次类推。注意reduce方法在python3中已经被移除
# def method3(s):
#     s_r = reduce(lambda x, y: y+x, s)
#     return s_r


# 方法四：使用递归方法
def method4(s):
    if len(s) < 1:
        return s
    return method4(s[1:])+s[0]


# 方法五：使用栈方法
def method5(s):
    s_l = list(s)   # 模拟入栈
    s_r = ''
    while len(s_l):
        s_r += s_l.pop(-1)  # 模拟出栈
    return s_r


# 方法六：使用for循环遍历：
def method6(s):
    n = len(s)
    s_r = ''
    for i in range(n):
        s_r += s[n-i-1]
    return s_r


s = input('请输入需要翻转的字符串：')
print('方法一的翻转结果：', method1(s))
print('方法二的翻转结果：', method2(s))
# print('方法三的翻转结果：', method3(s))
print('方法四的翻转结果：', method4(s))
print('方法五的翻转结果：', method5(s))
print('方法六的翻转结果：', method6(s))