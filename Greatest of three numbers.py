class Solution:
    def greatestOfThree(self,A,B,C):
        if(A > B and A>C):
             return A
        if(B> A and B>C):
            return B;
        else:
            return C;
