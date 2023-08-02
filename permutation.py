import itertools
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        return list(itertools.permutations(nums, len(nums)))

# Example input
if __name__ == "__main__":
    nums = [1, 2, 3]
    solution = Solution()
    result = solution.permute(nums)
    print(result)
