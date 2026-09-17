from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        for i, num in enumerate(nums):
            is_repeated = i > 0 and num == nums[i-1]
            if is_repeated:
                continue
            left, right = i+1, len(nums)-1
            while left < right:
                current_sum = num + nums[left] + nums[right]
                if current_sum < 0:
                    left += 1
                elif current_sum > 0:
                    right -= 1
                else:
                    output.append([num, nums[left], nums[right]])
                    left += 1
                    while left < right and nums[left] == nums[left-1]:
                        left += 1
        return output