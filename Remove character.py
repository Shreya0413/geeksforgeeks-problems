#User function Template for python3

class Solution:
    def removeChars (ob, str1, str2):
        # code here 
        s=""
        for ch in str1:
            if ch in str2:
                continue
            s=s+ch #add that ch to s
        return s
        
