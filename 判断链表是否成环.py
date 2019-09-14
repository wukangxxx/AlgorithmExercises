# !\usr\bin\python3
# _*_ coding _*_
"""
判断链表是否成环，并返回入口位置
通过快慢指针是否相遇来判断链表是否成环
相遇点距环入口的距离等于头节点距环入口的距离
"""


class Solution(object):
    def detect_cycle(self, head):
        if head is None or head.next is None:
            return None
        p = slow = fast = head
        while fast.next or fast.next.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                while slow != p:
                    slow = slow.next
                    p = p.next
                return p
        return None
