#User function Template for python3

class Solution:
    def getNumber(self,B, N):
        digits = "0123456789ABCDEF"
        result = ""

        while N > 0:
            result = digits[N % B] + result
            N = N // B
            #three loop like first 282%16=17 remainder 10 =A next 17%16=1 remainder 1 next 1%16 = 0 remainder 1
        return result
