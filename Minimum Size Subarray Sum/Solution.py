import sys

class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """
        result = sys.maxsize
        left_idx = 0
        s = 0
        
        for i in range(len(nums)):
            s = s + nums[i]
            while(s>= target):
                result = min(result, (i-left_idx+1))
                s = s - nums[left_idx]
                left_idx = left_idx + 1
                        
        return (result if (result!=sys.maxsize) else 0)