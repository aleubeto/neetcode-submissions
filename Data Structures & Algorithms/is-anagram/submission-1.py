class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self._usingSort(s, t)

    def _usingSort(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        