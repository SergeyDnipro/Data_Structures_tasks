from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    flowers_idx = 0
    qty_flowerbed = len(flowerbed)
    if not qty_flowerbed and not n:
        return True
    if not qty_flowerbed:
        return False

    while flowers_idx < qty_flowerbed and n > 0:
        if qty_flowerbed == 1 and n == 1:
            if flowerbed[flowers_idx] == 0:
                return True
            else: return False
        if flowers_idx == 0 and (flowerbed[flowers_idx] == 0 and flowerbed[flowers_idx + 1] == 0):
            n -= 1
            flowers_idx += 2
            continue
        elif flowers_idx + 1 == qty_flowerbed - 1 and (flowerbed[flowers_idx] == 0 and flowerbed[flowers_idx + 1] == 0):
            n -= 1
            break
        elif flowers_idx + 1 < qty_flowerbed and (flowerbed[flowers_idx] == flowerbed[flowers_idx + 1] == flowerbed[flowers_idx - 1] == 0):
            n -= 1
            flowers_idx += 2
            continue
        flowers_idx += 1

    if n == 0:
        return True
    return False


def can_place_flowers_1(flowerbed: List[int], n: int) -> bool:
    flowers_idx = 0
    qty_flowerbed = len(flowerbed)
    flowers_cell_idx = []
    free_cell_idx = []

    for ind in range(qty_flowerbed):
        if flowerbed[ind] == 0:
            free_cell_idx.append(ind)
        else:
            flowers_cell_idx.append(ind)

    i = 0
    j = 0
    if not flowers_cell_idx and flowerbed:
        return True
    while i < len(free_cell_idx) and j <= len(flowers_cell_idx):
        if free_cell_idx[i] == 0 and flowers_cell_idx[j] > free_cell_idx[i] + 1:
            n -= 1
            print('zero pos', free_cell_idx[i])
            i += 2
        elif j < len(flowers_cell_idx) - 1 and free_cell_idx[i] - flowers_cell_idx[j] > 1 and free_cell_idx[i] - flowers_cell_idx[j + 1] < -1:
            n -= 1
            print('inner pos', free_cell_idx[i])
            i += 2
        elif j == len(flowers_cell_idx) - 1 and free_cell_idx[i] - flowers_cell_idx[j] > 1:
            n -= 1
            print('after pos', free_cell_idx[i])
            i += 2
        elif free_cell_idx[i] - flowers_cell_idx[j] <= 1:
            i += 1
        else:
            j += 1

    if n < 1 :
        return True
    return False


f = []
n = 1

print(can_place_flowers_1(f, n))
