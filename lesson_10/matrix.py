arr = [
    [1, 2, 3, 12],
    [4, 5, 6, 5],
    [7, 8, 9, 3]
]

rows = len(arr)
cols = len(arr[0])

route = []
route_matr = [[0 for i in range(cols)] for j in range(rows)]

for row in range(rows):
    for col in range(cols):
        if row == 0 and col == 0:
            route_matr[row][col] = arr[row][col]
            continue
        elif row == 0:
            route_matr[row][col] = route_matr[row][col - 1] + arr[row][col]
        elif col == 0:
            route_matr[row][col] = route_matr[row - 1][col] + arr[row][col]
        else:
            route_matr[row][col] = min(route_matr[row - 1][col], route_matr[row][col - 1]) + arr[row][col]

print(*route_matr, sep='\n')
i = len(route_matr) - 1
j = len(route_matr[0]) - 1

while i >= 0 and j >= 0:
    route.append(arr[i][j])
    if i == 0:
        j -= 1
    elif j == 0:
        i -= 1
    else:
        if route_matr[i - 1][j] < route_matr[i][j - 1]:
            i = i - 1
        else:
            j = j - 1
print(route)