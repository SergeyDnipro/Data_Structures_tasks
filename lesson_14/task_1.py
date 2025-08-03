from typing import List


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

print(has_valid_path(n=3, edges=[[0, 1]], source=0, destination=2))