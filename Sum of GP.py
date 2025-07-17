class Solution:
	def sum_of_gp(self, n, a, r):
		if r == 1:
            return n*a
        elif r > 1:
            return int((a*(r**n-1))/(r-1))
        elif r < 1:
            return int((a*(1-r**n))/(1-r))
