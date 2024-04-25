'''
206.反转链表

给你单链表的头节点 head ，请你反转链表，并返回反转后的链表。

92.反转链表 II

给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre
    
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        cur = dummy
        for i in range(left-1):
            cur = cur.next
        cc = cur
        cur = cur.next
        pre = None
        for _ in range(right-left+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        cc.next.next = cur
        cc.next = pre
        return dummy.next