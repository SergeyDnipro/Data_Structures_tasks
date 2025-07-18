l1 = [5, 3, -2, 0, 1 , 4]

for ind in range(1, len(l1)):
    key = l1[ind]
    j = ind - 1
    while j >= 0 and l1[j] > key:
        l1[j + 1] = l1[j]
        j -=1
    l1[j + 1] = key

print(l1)
