# !\usr\bin\python3
# -*- coding:utf-8 -*-
"""
判断一个二叉树是否平衡
"""


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def TreeHeight(self, pRoot):
        if pRoot == None:
            return 0
        elif pRoot.left == None and pRoot.right == None:
            return 1
        else:
            lh = self.TreeHeight(pRoot.left)        # 使用递归算法求树的高度
            rh = self.TreeHeight(pRoot.right)
            return max(lh, rh) + 1                  # 因为根节点已包含一层

    def IsBalanced_Solution(self, pRoot):
        if pRoot is None:
            return True
        else:
            return abs(self.TreeHeight(pRoot.left) -         # 平衡二叉树的判断方法
                       self.TreeHeight(pRoot.right)) <= 1    # 左右子树高度差不大于1
