from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height: return
        result = 0
        left, right = 0, len(height)-1
        top_left, top_right = height[left], height[right]
        while left < right:
            if top_left < top_right:
                left += 1
                top_left = max(top_left, height[left])
                result += top_left - height[left]
            else:
                right -= 1
                top_right = max(top_right, height[right])
                result += top_right - height[right]
        return result
