#User function Template for python3

class Solution:
    def countOfElements(self, x, arr):
        count=0
        for i in arr:
            if(i<=x):
                count=count+1
        return count

