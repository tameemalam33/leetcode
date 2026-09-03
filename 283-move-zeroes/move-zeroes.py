class Solution(object):
    def moveZeroes(self, nums):
        left=0
        right=0
        for i in range(len(nums)):
            if nums[right] != 0:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right+=1
            else:
                right+=1

        