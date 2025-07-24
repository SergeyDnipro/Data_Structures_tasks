from typing import List


def can_jump(nums: List[int]) -> bool:
    if not nums or not isinstance(nums, list):
        return False
    n = len(nums)
    start_idx = 0
    end_idx = n - 1
    current_idx = 0
    while start_idx < end_idx:
        start_idx += nums[current_idx]
        if start_idx > end_idx or nums[current_idx] == 0:
            return False
        current_idx = start_idx
    return True

print(can_jump([3,2,1,0,4]))