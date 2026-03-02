#heap sort

def heapify(list_a, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and list_a[left] > list_a[largest]:
        largest = left

    if right < n and list_a[right] > list_a[largest]:
        largest = right

    if largest != i:
        list_a[i], list_a[largest] = list_a[largest], list_a[i]
        heapify(list_a, n, largest)


def heap_sort(list_a):
    n = len(list_a)

    # build a max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(list_a, n, i)

    # extract elements one by one
    for i in range(n - 1, 0, -1):
        list_a[0], list_a[i] = list_a[i], list_a[0]
        heapify(list_a, i, 0)

    return list_a



list_a = [6, 7, 8, 7, 6, 5, 4, 5, 6, 7, 6, 7, 8, 9, 7, 9, 0]

print(f"Before sorting: {list_a}")
print(f"After sorting: {heap_sort(list_a)}")
