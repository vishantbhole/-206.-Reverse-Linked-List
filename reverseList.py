# 206. Reverse Linked List
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
# Solution class with reverseList method
class Solution:
    def reverseList(self, head):
        prev, curr = None, head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

# Helper function to print linked list
def print_linked_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))


# Main block to test the code
if __name__ == "__main__":
    # Create linked list 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_linked_list(head)

    # Reverse the list
    solution = Solution()
    reversed_head = solution.reverseList(head)

    print("Reversed list:")
    print_linked_list(reversed_head)

