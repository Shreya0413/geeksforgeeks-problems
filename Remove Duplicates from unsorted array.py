class Solution:
    def removeDuplicate(self, arr):
        result = []
        for num in arr:
            if num not in result:
                result.append(num)
        return result
