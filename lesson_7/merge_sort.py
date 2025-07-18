def merge_sort(array):
    if len(array) <= 1:
        return array
    middle = len(array) // 2
    left = merge_sort(array[:middle])
    right = merge_sort(array[middle:])

    return merge(left, right)


def merge(left, right):
    i = j = 0
    sorted_array = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
