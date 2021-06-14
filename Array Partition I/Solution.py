class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # Sort Array
        nums.sort()
        
        # Every even element will be the minimum in a pair
        s=0
        for i in range(0,len(nums),2):
            s = s + nums[i]
        
        return s