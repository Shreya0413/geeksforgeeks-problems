class Solution:
    def logicalOperation (self, A, B, C, D, E, F):
        if ((not A) and B) + (C and D) + (E and (not F)):
            return 1
        return 0
