# Shell Sort Algorithm

def shell_sort(arr):
    """
    Shell Sort is a generalized version of insertion sort. 
    It starts by sorting pairs of elements far apart from each other, 
    then progressively reduces the gap between elements to be compared.
    """
    n = len(arr)
    gap = n // 2
    
    # Start with a big gap, then reduce the gap
    while gap > 0:
        # Do a gapped insertion sort for this gap size.
        # The first gap elements a[0..gap-1] are already in gapped order
        # keep adding one more element until the entire array is gap sorted
        for i in range(gap, n):
            # add a[i] to the elements that have been gap sorted
            # save a[i] in temp and make a hole at position i
            temp = arr[i]
            
            # shift earlier gap-sorted elements up until the correct location for a[i] is found
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            
            # put temp (the original a[i]) in its correct location
            arr[j] = temp
        gap //= 2
    return arr

if __name__ == "__main__":
    # Test cases
    test_list = [12, 34, 54, 2, 3]
    print(f"Original list: {test_list}")
    sorted_list = shell_sort(test_list.copy())
    print(f"Sorted list:   {sorted_list}")
    
    test_list_2 = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nOriginal list: {test_list_2}")
    sorted_list_2 = shell_sort(test_list_2.copy())
    print(f"Sorted list:   {sorted_list_2}")
