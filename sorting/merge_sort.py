#merge sort

def merge(left, right):
    sorted_list = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_list.append(left[left_index])
            left_index += 1
        else:
            sorted_list.append(right[right_index])
            right_index += 1
    
    sorted_list.extend(left[left_index:])
    sorted_list.extend(right[right_index:])
    
    return sorted_list

def merge_sort(list_a):
    if len(list_a) == 0 or len(list_a) == 1:
        return list_a
    
    middle_index = len(list_a) // 2
    left = list_a[:middle_index]
    right = list_a[middle_index:]
    
    return merge(merge_sort(left), merge_sort(right)) 



list_a = [6,7,8,7,6,5,4,5,6,7,6,7,8,9,7,9,0]
print(f"Before sorting: {list_a}")
print(f"After sorting: {merge_sort(list_a)}")