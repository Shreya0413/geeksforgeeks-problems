class Solution:
    def reciprocalString(self, S):
        s1=""
        for i in S:
            if i.isupper():
                s1=s1+chr(ord("A")+ord("Z")-ord(i))
            elif i.islower():
                s1=s1+chr(ord("a")+ord("z")-ord(i))
            else:
                s1=s1+i
        return s1
