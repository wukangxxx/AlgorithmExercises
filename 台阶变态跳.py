# !\usr\bin\python3
# -*- coding:utf-8 -*-
"""
n个台阶变态跳（一次能跳1、2、3、...、n阶）
"""


class Solution:
    def jumpFloorII(self, number):
        # write code here
        if number == 1 or number == 2:
            return number
        else:
            ans = 2    # jumpFloor(2)的结果
            for i in range(3, number+1):    # 从3~number
                tmp = ans    # 将前一步的结果赋值给tmp
                ans = tmp + ans
            return ans


n = int(input())
s = Solution()
s.jumpFloorII(n)