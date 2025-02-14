# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        final_ListNode = ListNode()
        current = final_ListNode
        carry = 0

        while l1 or l2 or carry:
            value1 = l1.val if l1 else 0
            value2 = l2.val if l2 else 0

            value = carry + value1 + value2
            carry = value // 10
            current.next = ListNode(value % 10)
            current = current.next

            if l1:
                l1 = l1.next 
            if l2:
                l2 = l2.next

        return final_ListNode.next