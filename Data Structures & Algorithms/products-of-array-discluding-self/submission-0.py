class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        newArr = [1] * len(nums)
        rightMult = 1
        leftMult = 1
        # Multiply and store right element to newArr to index 0
        for i in range(len(nums) - 1, -1, -1):
            newArr[i] *= rightMult
            rightMult *= nums[i]

        # Multiply and store left element to newArr to len(nums)
        for i in range(len(nums)):
            newArr[i] *= leftMult
            leftMult *= nums[i]
        return newArr