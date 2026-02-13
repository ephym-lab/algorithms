#quick sort

def quick_sort(list_a):
    if len(list_a) <= 1:
        return list_a
    
    pivot = list_a.pop()
    items_greater = []
    items_lower = []
    
    for item in list_a:
        if item > pivot:
            items_greater.append(item)
        else:
            items_lower.append(item)
    
    return quick_sort(items_lower) + [pivot] + quick_sort(items_greater)

list_a = [6,7,8,7,6,5,4,5,6,7,6,7,8,9,7,9,0]
print(f"Before sorting: {list_a}")
print(f"After sorting: {quick_sort(list_a)}")
