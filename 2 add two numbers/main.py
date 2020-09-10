# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode()
        temp = node
        carry = 0
        if l1 != None:
            l1val = l1.val
        else:
            l1val = 0
        if l2 != None:
            l2val = l2.val
        else:
            l2val = 0
        while (l1 != None or l2 != None):
            val = l1 + l2 + carry








temp = Solution()
temp.addTwoNumbers()

