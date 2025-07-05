class Solution:
    def isDigitSumPalindrome(self, n):
         s = 0
         for digit in str(n):
            s += int(digit)

        # Step 2: Check if the sum is a palindrome
         return str(s) == str(s)[::-1]
