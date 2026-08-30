class Solution(object):
    def reverseVowels(self,a):
        s=list(a)
        left=0
        right=len(s)-1
        while left<right:
            if s[left] not in "AEIOUaeiou":
                left+=1
            elif s[right] not in "AEIOUaeiou":
                right-=1
            elif s[left] in "AEIOUaeiou" and s[right] in "AEIOUaeiou":
                s[left],s[right]=s[right],s[left]

                left+=1
                right-=1
        return "".join(s)
       