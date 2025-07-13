from typing import List

class TwoSumSolver:
    @staticmethod
    def find_two_sum(nums: List[int], target: int) -> List[int]:
        solve = []

        for begin_index in range(len(nums) - 1):
            for end_index in range(begin_index + 1, len(nums)):
                temp_sum = nums[begin_index] + nums[end_index]
                if temp_sum == target:
                    solve.extend([begin_index, end_index])

        return solve

d1 = TwoSumSolver.find_two_sum([-100, -10, 16], 6)
print(d1)