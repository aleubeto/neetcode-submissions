class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [1] * len(nums)
        # [1, 2, 3, 4]
        # [<1>1, <1>2, <2>6, <6>12]
        # [24<24>, 24<12>, 12<8>, 4<6>]
        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            output[i] *= postfix
            postfix *= nums[i]
        return output