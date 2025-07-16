def quick_sort(unsorted_list, left_index, right_index):
    left = left_index
    right = right_index
    pivot = (left + right) // 2
    if left >= right:
        return

    while left < right:
        while unsorted_list[pivot] > unsorted_list[left] and left < pivot:
            left += 1
        while unsorted_list[pivot] < unsorted_list[right] and right > pivot:
            right -= 1
        if left < right:
            unsorted_list[right], unsorted_list[left] = unsorted_list[left], unsorted_list[right]
            print(pivot)
            print(unsorted_list)
            if pivot == left:
                pivot = right
                left += 1
            elif pivot == right:
                pivot = left
                right -= 1
            else:
                left += 1
                right -= 1
    quick_sort(unsorted_list, left_index, pivot - 1)
    quick_sort(unsorted_list, pivot + 1, right_index)

def quick_sort_array(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
    left_index = 0
    right_index = len(unsorted_list) - 1
    pivot = (left_index + right_index) // 2
    array_for_work = unsorted_list[:pivot] + unsorted_list[pivot+1:]

    left_array = [value for value in array_for_work if value < unsorted_list[pivot]]
    right_array = [value for value in array_for_work if value >= unsorted_list[pivot]]
    # print(left_array)
    # print(right_array)
    return quick_sort_array(left_array) + [unsorted_list[pivot]] + quick_sort_array(right_array)

our_list = [10, 9, -2, 0 , 1, 3, 11, 19, -8, 1]
our_list_1 = [10, 9, -2, 0 , 1, 3, 11, 19, -8]

res = quick_sort_array(our_list_1)
print(res)

# print(quick_sort(our_list, 0, len(our_list) - 1))