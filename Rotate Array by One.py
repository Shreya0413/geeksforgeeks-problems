class Solution:
    def rotate(self, arr):
        n = len(arr)
        k = 1   # rotate by one (clockwise)

        # Step 1: Reverse whole array
        arr.reverse()

        # Step 2: Reverse first k elements
        arr[:k] = reversed(arr[:k])

        # Step 3: Reverse remaining n-k elements
        arr[k:] = reversed(arr[k:])
