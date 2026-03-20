"""
Add Two Numbers (LeetCode #2)
==============================
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.

Example:
    Input:  l1 = [2, 4, 3]  (represents 342)
            l2 = [5, 6, 4]  (represents 465)
    Output: [7, 0, 8]       (represents 807)

Constraints:
    - The number of nodes in each linked list is in the range [1, 100].
    - 0 <= Node.val <= 9
    - It is guaranteed that the list represents a number that does not have leading zeros.

Time Complexity:  O(max(m, n))  — traverse both lists once
Space Complexity: O(max(m, n))  — result list length
"""

from __future__ import annotations
from typing import Optional


# ---------------------------------------------------------------------------
# Node definition
# ---------------------------------------------------------------------------

class ListNode:
    """A singly-linked list node."""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self) -> str:
        return f"ListNode({self.val})"


# ---------------------------------------------------------------------------
# Helper utilities
# ---------------------------------------------------------------------------

def list_to_linked(nums: list[int]) -> Optional[ListNode]:
    """Convert a Python list to a linked list and return the head node."""
    dummy = ListNode()
    current = dummy
    for n in nums:
        current.next = ListNode(n)
        current = current.next
    return dummy.next


def linked_to_list(head: Optional[ListNode]) -> list[int]:
    """Convert a linked list to a Python list for easy inspection."""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ---------------------------------------------------------------------------
# Solution
# ---------------------------------------------------------------------------

def add_two_numbers(
    l1: Optional[ListNode],
    l2: Optional[ListNode],
) -> Optional[ListNode]:
    """
    Add two numbers represented as reversed linked lists.

    Algorithm (Elementary addition with carry):
        1. Use a dummy head node so we never have to special-case the first node.
        2. Walk both lists simultaneously, summing corresponding digits + carry.
        3. Each iteration:
              digit_sum  = l1.val + l2.val + carry
              carry      = digit_sum // 10
              new_digit  = digit_sum  % 10
        4. Advance both pointers (treat an exhausted list as providing 0).
        5. After both lists are exhausted, if carry is still 1, append a final node.

    Args:
        l1: Head of the first linked list (digits in reverse order).
        l2: Head of the second linked list (digits in reverse order).

    Returns:
        Head of the resulting linked list (digits in reverse order).
    """
    dummy = ListNode(0)   # sentinel node — result built after this
    current = dummy
    carry = 0

    while l1 is not None or l2 is not None or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        digit_sum = val1 + val2 + carry
        carry = digit_sum // 10
        current.next = ListNode(digit_sum % 10)

        current = current.next
        if l1:
            l1 = l1.next
        if l2:
            l2 = l2.next

    return dummy.next


# ---------------------------------------------------------------------------
# Tests
# ---------------------------------------------------------------------------

def run_tests() -> None:
    test_cases = [
        # (l1_digits, l2_digits, expected_digits, description)
        ([2, 4, 3], [5, 6, 4], [7, 0, 8],    "342 + 465 = 807"),
        ([0],       [0],       [0],            "0 + 0 = 0"),
        ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1],
                                               "9999999 + 9999 = 10009998"),
        ([1],       [9, 9],    [0, 0, 1],      "1 + 99 = 100"),
        ([5],       [5],       [0, 1],         "5 + 5 = 10"),
    ]

    print("=" * 55)
    print("  Add Two Numbers — Test Suite")
    print("=" * 55)

    passed = 0
    for l1_list, l2_list, expected, description in test_cases:
        l1 = list_to_linked(l1_list)
        l2 = list_to_linked(l2_list)

        result_node = add_two_numbers(l1, l2)
        result = linked_to_list(result_node)

        status = "PASS" if result == expected else "FAIL"
        if status == "PASS":
            passed += 1

        print(f"  [{status}] {description}")
        if status == "FAIL":
            print(f"         Expected : {expected}")
            print(f"         Got      : {result}")

    print("=" * 55)
    print(f"  {passed}/{len(test_cases)} tests passed")
    print("=" * 55)


if __name__ == "__main__":
    run_tests()
