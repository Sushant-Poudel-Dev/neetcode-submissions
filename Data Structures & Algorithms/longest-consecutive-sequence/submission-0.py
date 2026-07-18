class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        hashset = set(nums)
        longestCon = 0
        for num in nums:
            if (num-1) not in hashset:
                currentNum = num
                currentLength = 1
                while (currentNum + 1) in hashset:
                    currentNum += 1
                    currentLength += 1
                    num += 1
                longestCon = max(longestCon, currentLength)
        return longestCon