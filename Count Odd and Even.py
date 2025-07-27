class Solution:
    def countOddEven(self, arr):
        count_even = 0
        count_odd = 0
        for num in arr:
            if num % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
        return count_odd, count_even
