class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        frequencyHashmap = defaultdict(int)

        for n in nums:
            frequencyHashmap[n] += 1

        bucket = [[] for _ in range(len(nums) + 1)]

        for num, count in frequencyHashmap.items():
            bucket[count].append(num)

        result = []
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
