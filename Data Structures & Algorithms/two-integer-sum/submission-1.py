class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexes = dict()
        for index, value in enumerate(nums):
            diff = target - value
            if diff in indexes.keys():
                return [indexes.get(diff), index]
            else:
                indexes[nums[index]] = index
