class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        while head and head.next:
            cur1 = head.next
            head.next = cur1.next
            cur1.next =  head
            prev.next = cur1
            prev = head
            head = head.next
        return dummy.next
def print_linked_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4))))
solution = Solution()
print("Original linked list:")
print_linked_list(head)
new_head = solution.swapPairs(head)
print("\nLinked list after swapping pairs:")
print_linked_list(new_head)