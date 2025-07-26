#User function Template for python3
class Solution:
    # Function to find values in array equal to their indices
    def valueEqualToIndex(self, arr):
        l=[]
        for i in range(len(arr)):
            index=i+1 # 1-based indexing # if 0 bases then index = i
            if index==arr[i]:
                l.append(index)
        return l
