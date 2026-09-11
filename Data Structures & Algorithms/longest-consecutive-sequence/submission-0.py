class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numsSet = set(nums)
        for num in nums:
            start_of = (num-1) not in numsSet
            lenght = 0
            if start_of:
                while (num+lenght) in numsSet:
                    lenght += 1
                longest = max(lenght, longest)

        return longest