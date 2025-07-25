from typing import List


def find_content_children(g: List[int], s: List[int]):
    children_list = sorted(g, reverse=True)
    cookie_list = sorted(s, reverse=True)

    children_idx = 0
    cookie_idx = 0
    count = 0

    while children_idx < len(children_list) and cookie_idx < len(cookie_list):
        if children_list[children_idx] <= cookie_list[cookie_idx]:
            children_idx += 1
            count += 1
            cookie_idx += 1
        else:
            children_idx += 1
    return count



g = [31,31,31]
s = [10, 20, 30, 32]

print(find_content_children(g, s))