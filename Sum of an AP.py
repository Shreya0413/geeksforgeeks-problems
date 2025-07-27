
class Solution:
    def nthTermOfAP(self, a1 : int, a2 : int, n : int) -> int:
        diff = a2 - a1
        result = (a1-diff) + (n*diff)
        return result
