class Solution:
    def reverseWords(self, s):
        words = [word for word in s.split('.') if word]
        reversed_words = words[::-1]
        return '.'.join(reversed_words)


