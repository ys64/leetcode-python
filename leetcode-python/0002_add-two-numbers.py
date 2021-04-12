# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        return str(self.val) + (self.next.__str__() if self.next != None else "")


class Solution:
    # 07/21/2020
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        temp = ans = ListNode()
        carry_over = 0
        first = True
        while ((l1 is not None) or (l2 is not None)) or carry_over != 0:
            val1 = 0 if l1 is None else l1.val
            val2 = 0 if l2 is None else l2.val
            val = (val1 + val2 + carry_over) % 10
            carry_over = (val1 + val2 + carry_over) // 10

            if first:
                ans.val = val
                first = False
            else:
                ans.next = ListNode(val)
                ans = ans.next

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        return temp


class Solution2:
    # 04/12/2021
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # carry over
        carry = 0
        placeholder = ans = ListNode()

        while l1 is not None or l2 is not None or carry != 0:
            val = (
                (l1.val if l1 is not None else 0)
                + (l2.val if l2 is not None else 0)
                + carry
            )
            temp = ListNode(int(val % 10))
            ans.next = temp
            ans = temp
            carry = int(val / 10)

            l1 = None if l1 is None else l1.next
            l2 = None if l2 is None else l2.next

        return ListNode() if placeholder.next == None else placeholder.next


l1 = ListNode(2, ListNode(4, ListNode(3)))
l2 = ListNode(5, ListNode(6, ListNode(4)))

s = Solution()
print(s.addTwoNumbers(l1, l2))

s2 = Solution2()
print(s2.addTwoNumbers(l1, l2))
