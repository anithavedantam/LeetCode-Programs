# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        length = -1
        curr = dummy = head
        while dummy:
            length += 1
            dummy = dummy.next
        value = 0
        while length >= 0 and curr:
            value += curr.val * (2 ** length)
            length -= 1
            curr = curr.next
        return value