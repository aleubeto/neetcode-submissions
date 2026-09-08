class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return self._usingDict(s, t)

    def _usingDict(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dictS, dictT = {}, {}
        for i in range(len(s)):
            dictS[s[i]] = dictS.get(s[i], 0) + 1
            dictT[t[i]] = dictT.get(t[i], 0) + 1
        for key in dictS:
            if dictS[key] != dictT.get(key, 0):
                return False
        return True
