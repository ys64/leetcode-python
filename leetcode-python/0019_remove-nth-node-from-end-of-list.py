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

    def __eq__(self, other):
        while self.next is not None or other.next is not None:
            if self.val != other.val:
                return False

            if self.next is None:
                return False
            else:
                self = self.next

            if other.next is None:
                return False
            else:
                other = other.next

        return True


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


class Solution2:
    # 4/13/2021
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        placeholder = head

        length = 1
        while head.next is not None:
            head = head.next
            length += 1

        # reset the pointer of head to first
        head = placeholder

        if length == 1:
            placeholder = None
        elif n == 1:
            # case: remove last node
            for i in range(length):
                if i == length - n - 1:
                    head.next = None
                    break

                if head.next is not None:
                    head = head.next
        else:
            for i in range(length):
                if i == length - n:
                    if head.next is not None:
                        head.val = head.next.val
                        head.next = head.next.next
                    break

                if head.next is not None:
                    head = head.next

        return placeholder


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


import pytest


@pytest.mark.parametrize(
    ("head", "n", "expected"),
    [
        (
            ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5))))),
            2,
            ListNode(1, ListNode(2, ListNode(3, ListNode(5)))),
        ),
        (ListNode(1, ListNode(2, ListNode(3))), 1, ListNode(1, ListNode(2))),
        (ListNode(1), 1, None),
    ],
)
def test_solution(head, n, expected):
    s = Solution()
    assert s.removeNthFromEnd(head, n) == expected
