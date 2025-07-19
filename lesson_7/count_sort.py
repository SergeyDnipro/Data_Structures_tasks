from collections import defaultdict


count_dict = defaultdict(int)
list1 = [7, 3, 1, -2, 0, 11, -4, 5, 2, 3, 1]

min_num = min(list1)
max_num = max(list1)

for i in list1:
    count_dict[i] += 1

num_dict = {key: count_dict.get(key, 0) for key in range(min_num, max_num + 1)}

sorted_array = []

for key, value in num_dict.items():
    if value:
        sorted_array.extend([key] * value)

print(num_dict)
print(sorted_array)




