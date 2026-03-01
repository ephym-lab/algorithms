# Interpolation Search Algorithm
# Time Complexity: O(log log n) average for uniform data, O(n) worst case
# Space Complexity: O(1) iterative, O(n) recursive worst case
#
# Unlike binary search which always picks the midpoint,
# interpolation search estimates WHERE the target is likely
# to be based on the value distribution — similar to how
# you'd look up a name in a phone book.


def interpolation_search_iterative(arr, target):
    """
    Iterative interpolation search.

    Uses the interpolation formula to estimate the position
    of the target based on the values at the boundaries.

    Args:
        arr: A sorted list of uniformly distributed elements.
        target: The element to search for.

    Returns:
        The index of the target if found, otherwise -1.
    """
    low, high = 0, len(arr) - 1

    while low <= high and arr[low] <= target <= arr[high]:
        # Avoid division by zero when all elements are the same
        if arr[low] == arr[high]:
            if arr[low] == target:
                return low
            break

        # Interpolation formula — estimate the position
        pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

        if arr[pos] == target:
            return pos
        elif arr[pos] < target:
            low = pos + 1
        else:
            high = pos - 1

    return -1


def interpolation_search_recursive(arr, target, low, high):
    """
    Recursive interpolation search.

    Args:
        arr: A sorted list of uniformly distributed elements.
        target: The element to search for.
        low: Lower boundary index.
        high: Upper boundary index.

    Returns:
        The index of the target if found, otherwise -1.
    """
    if low > high or target < arr[low] or target > arr[high]:
        return -1

    if arr[low] == arr[high]:
        if arr[low] == target:
            return low
        return -1

    # Interpolation formula
    pos = low + ((target - arr[low]) * (high - low)) // (arr[high] - arr[low])

    if arr[pos] == target:
        return pos
    elif arr[pos] < target:
        return interpolation_search_recursive(arr, target, pos + 1, high)
    else:
        return interpolation_search_recursive(arr, target, low, pos - 1)


# ──────────────────────────────────────────────
# Driver Code
# ──────────────────────────────────────────────

def main():
    # Uniformly distributed sorted array (best case for interpolation search)
    arr = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

    print("Sorted Array:", arr)
    print("=" * 55)

    # --- Iterative search ---
    target = 70
    result = interpolation_search_iterative(arr, target)
    if result != -1:
        print(f"[Iterative] Element {target} found at index {result}")
    else:
        print(f"[Iterative] Element {target} not found")

    # --- Recursive search ---
    target = 30
    result = interpolation_search_recursive(arr, target, 0, len(arr) - 1)
    if result != -1:
        print(f"[Recursive] Element {target} found at index {result}")
    else:
        print(f"[Recursive] Element {target} not found")

    # --- Element not in array ---
    target = 55
    result = interpolation_search_iterative(arr, target)
    if result != -1:
        print(f"[Iterative] Element {target} found at index {result}")
    else:
        print(f"[Iterative] Element {target} not found")

    # --- Edge: first element ---
    target = 10
    result = interpolation_search_iterative(arr, target)
    print(f"[Iterative] First element {target} found at index {result}")

    # --- Edge: last element ---
    target = 100
    result = interpolation_search_iterative(arr, target)
    print(f"[Iterative] Last element {target} found at index {result}")

    # --- Non-uniform array still works ---
    arr2 = [2, 5, 13, 19, 27, 44, 78, 102, 350, 911]
    print(f"\nNon-uniform Array: {arr2}")
    print("=" * 55)

    target = 44
    result = interpolation_search_iterative(arr2, target)
    if result != -1:
        print(f"[Iterative] Element {target} found at index {result}")
    else:
        print(f"[Iterative] Element {target} not found")

    target = 911
    result = interpolation_search_recursive(arr2, target, 0, len(arr2) - 1)
    if result != -1:
        print(f"[Recursive] Element {target} found at index {result}")
    else:
        print(f"[Recursive] Element {target} not found")


if __name__ == "__main__":
    main()
