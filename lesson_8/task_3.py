from typing import List
from collections import deque


def count_students(students: List[int], sandwiches: List[int]) -> int:
    if not students and not sandwiches:
        return 0
    students_qty_1 = students.count(1)
    students_qty_0 = students.count(0)
    sandwiches_qty_1 = sandwiches.count(1)
    sandwiches_qty_0 = sandwiches.count(0)

    if sandwiches_qty_1 >= students_qty_1 and sandwiches_qty_0 >= students_qty_0:
        return 0

    if students_qty_1 - sandwiches_qty_1 == students_qty_1 > 0 == students_qty_0:
        return students_qty_1
    elif students_qty_0 - sandwiches_qty_0 == students_qty_0 > 0 == students_qty_1:
        return students_qty_0

    if len(students) - len(sandwiches) == 1:
        return 1

    if len(sandwiches) == 1 and sandwiches[0] == students[0]:
        return len(students) - 1

    if len(students) == students_qty_1 and sandwiches_qty_1 < students_qty_1:
        return students_qty_1

    students_deque = deque(students)
    sandwiches_deque = deque(sandwiches)

