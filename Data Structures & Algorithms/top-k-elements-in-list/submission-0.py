class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = dict()
        ranking = [[] for i in range(len(nums) + 1)]

        for num in nums:
            frequencies[num] = frequencies.get(num, 0) + 1
        for num, frequency in frequencies.items():
            ranking[frequency].append(num)

        top_k_values = []
        for rank in range(len(ranking) -1, 0, -1):
            for num in ranking[rank]:
                top_k_values.append(num)
                if len(top_k_values) == k:
                    return top_k_values
