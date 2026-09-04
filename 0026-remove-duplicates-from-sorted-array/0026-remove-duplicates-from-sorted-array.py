class Solution(object):
  def removeDuplicates(self, nums):
    x=nums
    left=0
    right=1
    while right<len(x):
        if x[left]!=x[right]:
            left+=1
            x[left]=x[right]
        else:
            right+=1
    return left+1    


        