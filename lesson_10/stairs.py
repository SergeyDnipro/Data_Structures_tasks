import numpy as np

def calculate_stairs(qty_of_stairs: int):
    calc_array = np.zeros(qty_of_stairs)
    stairs(calc_array, qty_of_stairs - 1)
    return calc_array

def stairs(calc_array: np.array, n:int):
    if calc_array[n] > 0:
        return
    if n == 0:
        calc_array[n] = 1
    elif n == 1:
        calc_array[n] = 2
    elif n == 2:
        calc_array[n] = 4
    else:
        stairs(calc_array, n - 1)
        stairs(calc_array, n - 2)
        stairs(calc_array, n - 3)
        calc_array[n] = calc_array[n - 1] + calc_array[n - 2] + calc_array[n - 3]

print(calculate_stairs(10))

