# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self) -> str:
        if self.next is None:
            return str(self.val)
        else:
            return str(self.val) + " -> " + self.next.__str__()


class Solution:
    # 09/01/2020
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 1
        node = head.next
        while node is not None:
            count += 1
            node = node.next

        temp = node = head

        if count == n:
            temp = temp.next
        else:
            for i in range(count):
                if i == (count - 1 - n):
                    # skip
                    node.next = node.next.next
                    break

                node = node.next

        return temp


class ModelSolution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        count = 1
        node = head.next
        while node is not None:
            count += 1
            node = node.next

        temp = node = head

        if count == n:
            temp = temp.next
        else:
            for i in range(count):
                if i == (count - 1 - n):
                    # skip
                    node.next = node.next.next
                    break

                node = node.next

        return temp


s = Solution()
head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
n = 2
print(s.removeNthFromEnd(head, n))

head = ListNode(1, ListNode(2, ListNode(3)))
n = 1
print(s.removeNthFromEnd(head, n))

head = ListNode(1)
n = 1
print(s.removeNthFromEnd(head, n))
