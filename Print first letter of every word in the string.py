#User function Template for python3
class Solution:
	def firstAlphabet(self, S):
		# code here
	    s=''
        w=S.split()
        for i in w:
            s+=i[0] # in string no add()
        return s
