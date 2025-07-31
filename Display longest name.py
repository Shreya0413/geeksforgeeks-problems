
class Solution:
    def longest(self, arr):
        # code here
        ans = ''
        # code here
        for x in arr:
            if(len(x) > len(ans)):
                ans = x
        
        return ans
