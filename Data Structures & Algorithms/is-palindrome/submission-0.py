class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s)-1
        while left < right:
            while left < right and not self._is_alpha_numerical(s[left]):
                left += 1
            while right > left and not self._is_alpha_numerical(s[right]):
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        return True

    def _is_alpha_numerical(self, char: str) -> bool:
        is_upper_case = (ord("A") <= ord(char) <= ord("Z"))
        is_lower_case = (ord("a") <= ord(char) <= ord("z"))
        is_numeric = (ord("0") <= ord(char) <= ord("9"))
        return is_upper_case or is_lower_case or is_numeric