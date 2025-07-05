class Solution:
    def isInRange(ob, N):
        words = ["one", "two", "three", "four", "five", 
                 "six", "seven", "eight", "nine", "ten"]
        
        if 1 <= N <= 10:
            return words[N - 1]
        else:
            return "not in range"
