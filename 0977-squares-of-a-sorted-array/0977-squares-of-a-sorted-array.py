class Solution(object):
    def sortedSquares(self, nums):
        neg=[]
        pos=[]
        for i in range(len(nums)):
            if nums[i]<0:
                neg.append(nums[i])
            else:
                pos.append(nums[i])
        if len(neg)==0:
            return [x*x for x in pos]
        elif len(pos)==0:
            res=[x*x for x in neg]
            res.reverse()
            return res
        else:
            neg=[x*x for x in neg][::-1]
            pos=[x*x for x in pos]
            res=[]
            i=0
            j=0
            while i<len(neg) and j <len(pos):
                if neg[i]<pos[j]:    
                    res.append(neg[i])
                    i+=1
                else:
                    res.append(pos[j])
                    j+=1
            while i<len(neg):
                res.append(neg[i])
                i+=1
            while j<len(pos):
                res.append(pos[j])
                j+=1
        return res


