# Link: https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curnode = head
        prevnode = None
        while curnode:
            tmpnode = curnode.next
            curnode.next = prevnode
            prevnode = curnode
            curnode = tmpnode
        return prevnode