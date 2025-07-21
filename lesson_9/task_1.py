from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    result_array = []
    for first_idx in range(len(nums) - 1):
        for second_idx in range(first_idx + 1, len(nums)):
            if nums[first_idx] + nums[second_idx] == target:
                result_array.extend([first_idx, second_idx])
    return result_array
    # your code