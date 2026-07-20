class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        result = []
        sortedNums = sorted(nums)
        for i in range(len(sortedNums)):
            left = i + 1
            right = len(nums) - 1
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                continue
            while left < right:
                currentSum = sortedNums[i] + sortedNums[left] + sortedNums[right]
                if currentSum < 0:
                    left += 1
                if currentSum > 0:
                    right -= 1
                if currentSum == 0:
                    result.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedNums[left] == sortedNums[left - 1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right + 1]:
                        right -= 1
        return result
