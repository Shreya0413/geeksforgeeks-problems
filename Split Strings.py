#User function Template for python3

class Solution:
    def splitString(ob, S): 
        S1 =""
        S2 =""
        S3 =""
        for i in S:
            if i.isalpha():
                S1 = S1+i
            elif i.isnumeric():
                S2 = S2+i
            else:
                S3 = S3+i
        return S1,S2, S3 
       
