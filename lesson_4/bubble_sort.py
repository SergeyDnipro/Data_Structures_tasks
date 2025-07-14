unsorted_list = [3, 1, -10, -9, 8, 0, 100, 2]

array_length = len(unsorted_list)

# for loop_count in range(array_length - 1):
#     for element in range(array_length - 1):
#         if unsorted_list[element] > unsorted_list[element + 1]:
#             unsorted_list[element], unsorted_list[element + 1] = unsorted_list[element + 1], unsorted_list[element]

for loop_index in range(array_length - 1):
    swap = False
    for element_index in range(array_length - loop_index - 1):
        if unsorted_list[element_index] > unsorted_list[element_index + 1]:
            unsorted_list[element_index], unsorted_list[element_index + 1] = unsorted_list[element_index + 1], unsorted_list[element_index]
            swap = True
    if not swap:
        break

print(unsorted_list)

