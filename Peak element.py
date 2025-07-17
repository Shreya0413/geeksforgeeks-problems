class Solution:   
    def peakElement(self,arr):
        n = len(arr)
        low, high = 0, n - 1

        while low <= high:
            mid = (low + high) // 2

            left = arr[mid - 1] if mid > 0 else float('-inf')
            right = arr[mid + 1] if mid < n - 1 else float('-inf')

            if arr[mid] >= left and arr[mid] >= right:
                return mid  # Found a peak

            if arr[mid] < right:
                low = mid + 1  # Peak must be on right side
            else:
                high = mid - 1  # Peak must be on left side

        return -1  # Should never reach here if input is valid
