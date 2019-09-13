# !\usr\bin\python3
# _*_ coding:utf-8 _*_
"""
判断一个字符串是否是回文
判断最长回文串
"""


def is_palindrome(s):
    n = len(s)
    l, r = 0, n-1
    while l < r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True


def longest_palindrome(s):
    maxl, n = 0, len(s)
    p = []
    for i in range(n):
        """回文长度为奇数"""
        k = 1
        while i-k >= 0 and i+k < n:
            if s[i-k] != s[i+k]:
                k = k - 1  # 因为前面k+1之后才不满足条件，故k需要-1才能满足条件
                break
            k += 1
        if 2*k+1 > maxl:
            maxl = 2*k+1
            p.append([maxl, s[i-k:i+k+1]])  # 切片因为左开右闭，所以右边需要+1
        """回文长度为奇数"""
        k = 0
        while i-k >= 0 and i+1+k < n:
            if s[i-k] != s[i+1+k]:
                k = k - 1  # 因为前面k+1之后才不满足条件，故k需要-1才能满足条件
                break
            k += 1
        if 2*k+2 > maxl:
            maxl = 2*k+2
            p.append([maxl, s[i-k:i+1+k+1]])    # 切片因为左开右闭，所以右边需要+1
    for p_ in p:
        if p_[0] == maxl:
            t = p_[1]
    return maxl, t, p


is_palindrome('asjdjsa')
longest_palindrome('qabcdefgfedcbaa')