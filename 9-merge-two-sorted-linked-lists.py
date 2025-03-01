from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        start = ListNode(0, None)
        sorted_list_head = start
        while list1 and list2:
            if list1.val < list2.val:
                start.next = list1
                list1 = list1.next
            else:
                start.next = list2
                list2 = list2.next
            start = start.next

        if list1:
            start.next = list1
        if list2:
            start.next = list2

        if not start.next:
            return None

        return sorted_list_head.next

    # TC - O(n+m)
    # Sc - O(1)


class Solution2:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list2:
            return list1
        if not list1:
            return list2
        if list1.val < list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2

    # TC - O(n+m)
    # SC - O(n+m) # Recursion stack space


class Solution3:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        start = ListNode(0, None)
        temp_start = start

        if list1.val < list2.val:
            start.next = list1
            start.next.next = self.mergeTwoLists(list1.next, list2)
        else:
            start.next = list2
            start.next.next = self.mergeTwoLists(list1, list2.next)

        if not temp_start.next:
            return None
        return temp_start.next

    # TC - O(n+m)
    # SC - O(n+m) # Recursion stack space


# URL - https://neetcode.io/problems/merge-two-sorted-linked-lists
