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
    # 07/14/2020
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None and l2 is None:
            return None

        temp = newlist = ListNode()
        while (l1 is not None) or (l2 is not None):
            if l1 is None:
                newlist.val = l2.val
                l2 = l2.next
            elif l2 is None:
                newlist.val = l1.val
                l1 = l1.next
            elif l1.val <= l2.val:
                newlist.val = l1.val
                l1 = l1.next
            else:
                newlist.val = l2.val
                l2 = l2.next

            if (l1 is not None) or (l2 is not None):
                newlist.next = ListNode()
                newlist = newlist.next

        return temp


class Solution2:
    # 04/13/2021
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        placeholder = temp = ListNode()

        while l1 is not None or l2 is not None:
            if l1 is None:
                temp.next = l2
                break

            if l2 is None:
                temp.next = l1
                break

            if l1.val <= l2.val:
                temp.next = ListNode(l1.val)
                temp = temp.next
                l1 = l1.next
            elif l2.val < l1.val:
                temp.next = ListNode(l2.val)
                temp = temp.next
                l2 = l2.next
            else:
                print("error")

        return placeholder.next


class ModelSolution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        prev = dummy = ListNode(None)  # new dummy head for the merged list

        while l1 and l2:  # link prev to the lowest node
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next

            prev = prev.next

        prev.next = l1 or l2  # link prev to the list with remaining nodes

        return dummy.next


s = Solution()
print(
    s.mergeTwoLists(
        ListNode(1, ListNode(2, ListNode(4))), ListNode(1, ListNode(3, ListNode(4)))
    )
)


import pytest


@pytest.mark.parametrize(
    ("l1", "l2", "expected"),
    [
        (
            ListNode(1, ListNode(2, ListNode(4))),
            ListNode(1, ListNode(3, ListNode(4))),
            ListNode(
                1, ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(4)))))
            ),
        ),
        (None, None, None),
        (None, ListNode(), ListNode()),
    ],
)
def test_solution(l1, l2, expected):
    s = Solution()
    assert s.mergeTwoLists(l1, l2) == expected
