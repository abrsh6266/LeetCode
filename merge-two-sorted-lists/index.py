# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        current = ListNode()
        temp = current
        while list1 != None or list2 != None:
            if list2 == None:
                temp.next = ListNode(list1.val)
                list1 = list1.next
                temp = temp.next
            elif list1 == None:
                temp.next = ListNode(list2.val)
                list2 = list2.next
                temp = temp.next
            elif list1.val <= list2.val:
                temp.next = ListNode(list1.val)
                list1 = list1.next
                temp = temp.next
            else:
                temp.next = ListNode(list2.val)
                list2 = list2.next
                temp = temp.next
        return current.next
        
        