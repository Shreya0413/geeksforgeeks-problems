class Solution:
    def maxWater(self, arr):
        # code here
        count=0
        left=0
        right=len(arr)-1
        left_max=0
        right_max=0
        
        while(left<right):
            left_max=max(left_max,arr[left])
            right_max=max(right_max,arr[right])
            
            if(left_max<right_max):
                count=count+(left_max-arr[left])
                left=left+1
            else:
                count=count+(right_max-arr[right])
                right=right-1
        return count
