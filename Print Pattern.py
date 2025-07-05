class Solution:
    def pattern(self, N):
        result = []

        def helper(n):
            result.append(n)
            if n <= 0:
                return
            helper(n - 5)
            result.append(n)

        helper(N)
        return result
