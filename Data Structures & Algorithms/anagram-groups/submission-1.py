from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = self._use_chart_count(strs)
        return list(anagrams.values())


    def _use_chart_count(self, strings_list: str) -> Dict:
        anagrams = defaultdict(list)
        for word in strings_list:
            firm = [0] * 26
            for char in word:
                firm[ord(char) - ord("a")] += 1
            anagrams[tuple(firm)].append(word)
        return(anagrams)