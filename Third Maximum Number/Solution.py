import sys

class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        if(len(nums) < 3):
            return max(nums)
        
        max_num_1 = max_num_2 = max_num_3 = -sys.maxint -1 
        
        for i in range(len(nums)):
            if(nums[i] != max_num_1 and nums[i] != max_num_2 and nums[i] != max_num_3):
                if(nums[i] > max_num_1 and nums[i] > max_num_2):
                    max_num_3 = max_num_2
                    max_num_2 = max_num_1
                    max_num_1 = nums[i]
                elif(nums[i] > max_num_2 and nums[i] > max_num_3):
                    max_num_3 = max_num_2
                    max_num_2 = nums[i]
                elif(nums[i] > max_num_3):
                    max_num_3 = nums[i]
        
        if(max_num_3 != -sys.maxint -1):
            return max_num_3 
        else:
            return max_num_1