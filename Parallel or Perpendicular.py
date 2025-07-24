#User function Template for python3

class Solution:
	def find(self, A, B):
        a1, a2, a3 = A
        b1, b2, b3 = B

        # Dot product
        dot = a1 * b1 + a2 * b2 + a3 * b3

        # Cross product squared
        cx = a2 * b3 - a3 * b2
        cy = a3 * b1 - a1 * b3
        cz = a1 * b2 - a2 * b1
        cross_sq = cx * cx + cy * cy + cz * cz

        if cross_sq == 0:
            return 1  # Parallel
        elif dot == 0:
            return 2  # Perpendicular
        else:
            return 0  # Neither
