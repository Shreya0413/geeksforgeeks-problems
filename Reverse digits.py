class Solution:
	def reverseDigits(self, n):
        reversed_str = str(n)[::-1]  # Reverse the digits using slicing
        return int(reversed_str)     # Convert back to int to remove leading zeroes
