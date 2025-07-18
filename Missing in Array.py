class Solution:
    def missingNum(self, arr):
        n=len(arr)+1 #as n-1 element is present
        total=n*(n+1)//2
        s=sum(arr)#sum
        return total-s #total-sum to get the number
