class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        # Make a copy
        copy = heights[:]
        copy.sort()
        
        count = 0
        for i in range(len(heights)):
            if(heights[i] != copy[i]):
                count = count +1
        
        return count