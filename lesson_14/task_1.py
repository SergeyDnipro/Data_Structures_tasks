from typing import List
from collections import defaultdict
from pprint import pprint


def has_valid_path(n: int, edges: List[List[int]], source: int, destination: int) -> bool:
    if source == destination:
        return True
    first_node = source
    for node in range(len(edges)):
        if first_node == edges[node][0]:
            first_node = edges[node][1]
            if first_node == destination:
                return True
    return False


def pathfinder(n: int, edges: List[List[int]], destination: int):
    adj_matrix = [[0 for i in range(n)] for j in range(n)]
    for edge in edges:
        adj_matrix[edge[0]][edge[1]] = 1
    pprint(adj_matrix)

    find_path_recursion(0, adj_matrix, destination)

def find_path_recursion(n: int, matr, destination: int):
    path.append(n)
    if n == destination:
        print(path)
        return
    for j in range(len(matr[n])):
        if matr[n][j] == 1:
            find_path_recursion(j, matr, destination)
    path.pop()


path = []
# def stack(n: int, destination: int):
#     stk.append(n)
#     print(stk)
#     if n != destination:
#         stack(n+1, destination)
#     stk.pop()
#     print(stk)



# stk = []
# stack(0, 5)
# n = 10
# path = {key: False for key in range(n)}
# print(path)
pathfinder(7, [[0, 1], [0, 2], [1, 3], [2, 4], [3, 5], [4, 6]], 5)