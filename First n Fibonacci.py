class Solution:
    # Function to return list containing first n fibonacci numbers.
    def fibonacciNumbers(self, n):
        if n <= 0:
            return []
        if n == 1:
            return [0]
        
        fib = [0, 1]
        for i in range(2, n):
            fib.append(fib[-1] + fib[-2]) #last element is denoted by [-1] and second last is [-2]
        return fib
