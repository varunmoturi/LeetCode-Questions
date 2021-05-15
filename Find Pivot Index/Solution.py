class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        
        # Get Sum of all elements in array
        total_sum = 0
        
        for i in nums:
           total_sum = total_sum + i
        
        # LooP through the list again checking for left sum and right sum
        
        left_sum = 0
        right_sum = 0
        
        for i in range(len(nums)):
            left_sum = left_sum + nums[i]
            right_sum = total_sum - left_sum
            
            if(left_sum - nums[i] == right_sum):
                return i
        
        return -1