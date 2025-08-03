from pprint import pprint
import numpy as np

edges = [[0,1],[0,2],[1,3],[1,2],[2,3]]
n = 4
matr = [[0 for i in range(n)] for j in range(n)]

for edge in edges:
    matr[edge[0]][edge[1]] = 1

print(np.array(matr))
