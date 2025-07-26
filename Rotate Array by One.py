class Solution:
    def rotate(self, arr):
        last = arr[-1]              # Get last element
        for i in range(len(arr)-1, 0, -1):
            arr[i] = arr[i-1]       # Shift elements right
        arr[0] = last               # Place last at the front
