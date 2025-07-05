class Solution:
    def isVowel (ob,c):
        for i in c:
            if i not in ['a','e','i','o','u','A','E','I','O','U']:
                return "NO"
            return "YES"
