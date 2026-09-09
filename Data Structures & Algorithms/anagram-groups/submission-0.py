from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = self._use_sort(strs)
        return list(anagrams.values())


    def _use_sort(self, strings_list: str) -> Dict:
        anagrams = defaultdict(list)
        for word in strings_list:
            firm = "".join(sorted(word))
            anagrams[firm].append(word)
        return anagrams
