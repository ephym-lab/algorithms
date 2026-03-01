# Binary Search Algorithm
# Time Complexity: O(log n)
# Space Complexity: O(1) iterative, O(log n) recursive
#
# Binary search works on sorted arrays by repeatedly dividing
# the search interval in half. It compares the target value to
# the middle element and eliminates half of the remaining
# elements each iteration.


def binary_search_iterative(arr, target):
    """
    Iterative binary search.

    Args:
        arr: A sorted list of elements.
        target: The element to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids potential overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def binary_search_recursive(arr, target, left, right):
    """
    Recursive binary search.

    Args:
        arr: A sorted list of elements.
        target: The element to search for.
        left: Left boundary index.
        right: Right boundary index.

    Returns:
        The index of the target if found, otherwise -1.
    """
    if left > right:
        return -1

    mid = left + (right - left) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def lower_bound(arr, target):
    """
    Finds the index of the first element >= target.

    Useful for range queries and finding insertion points.

    Args:
        arr: A sorted list of elements.
        target: The value to find the lower bound for.

    Returns:
        The index of the first element >= target,
        or len(arr) if all elements are smaller.
    """
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left


def upper_bound(arr, target):
    """
    Finds the index of the first element > target.

    Args:
        arr: A sorted list of elements.
        target: The value to find the upper bound for.

    Returns:
        The index of the first element > target,
        or len(arr) if no element is greater.
    """
    left, right = 0, len(arr)

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] <= target:
            left = mid + 1
        else:
            right = mid

    return left


# ──────────────────────────────────────────────
# Driver Code
# ──────────────────────────────────────────────

def main():
    arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 72, 91]

    print("Sorted Array:", arr)
    print("=" * 50)

    # --- Iterative search ---
    target = 23
    result = binary_search_iterative(arr, target)
    if result != -1:
        print(f"[Iterative] Element {target} found at index {result}")
    else:
        print(f"[Iterative] Element {target} not found")

    # --- Recursive search ---
    target = 56
    result = binary_search_recursive(arr, target, 0, len(arr) - 1)
    if result != -1:
        print(f"[Recursive] Element {target} found at index {result}")
    else:
        print(f"[Recursive] Element {target} not found")

    # --- Element not in array ---
    target = 99
    result = binary_search_iterative(arr, target)
    if result != -1:
        print(f"[Iterative] Element {target} found at index {result}")
    else:
        print(f"[Iterative] Element {target} not found")

    # --- Lower & Upper bound ---
    target = 16
    lb = lower_bound(arr, target)
    ub = upper_bound(arr, target)
    print(f"\nLower bound of {target}: index {lb} (value {arr[lb]})")
    print(f"Upper bound of {target}: index {ub} (value {arr[ub]})")

    # --- Count occurrences in a list with duplicates ---
    dupes = [1, 3, 3, 3, 5, 7, 7, 9]
    target = 3
    count = upper_bound(dupes, target) - lower_bound(dupes, target)
    print(f"\nOccurrences of {target} in {dupes}: {count}")


if __name__ == "__main__":
    main()
