class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        count=0
        max_count=count
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                max_count=max(max_count,count)
                count=0
        max_count=max(max_count,count)
        return max_count
        