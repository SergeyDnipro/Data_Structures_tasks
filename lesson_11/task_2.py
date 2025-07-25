from typing import List


def can_place_flowers(flowerbed: List[int], n: int) -> bool:
    flowers_idx = 0
    if not flowerbed and not n:
        return True
    if not flowerbed:
        return False

    while flowers_idx < len(flowerbed) and n > 0:
        if len(flowerbed) == 1 and n == 1:
            if flowerbed[flowers_idx] == 0:
                return True
            else: return False
        if flowers_idx == 0 and (flowerbed[flowers_idx] == 0 and flowerbed[flowers_idx + 1] == 0):
            n -= 1
            flowers_idx += 2
            continue
        elif flowerbed[flowers_idx] == 0 and flowerbed[flowers_idx - 1] == 0:
        elif flowerbed[flowers_idx] == flowerbed[flowers_idx + 1] == flowerbed[flowers_idx - 1] == 0:
            n -= 1
            flowers_idx += 2
            continue
        flowers_idx += 1
    if n == 0:
        return True
    return False


f = [1,0,0,0,1]
n = 1

print(can_place_flowers(f, n))