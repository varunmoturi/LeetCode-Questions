class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Return 0 i there is only one element in the array
        if(len(nums) == 1):
            return 0
        
        # Find the highest and 2nd highest numbers and their indexes in the array
        max_num_1 = 0
        max_num_1_idx = 0
        
        max_num_2 = 0
        max_num_2_idx = 0
        
        for i in range(len(nums)):
            if(nums[i] > max_num_1):
                max_num_2 = max_num_1
                max_num_2_idx = max_num_1_idx
                
                max_num_1 = nums[i]
                max_num_1_idx = i
            else:
                if(nums[i] > max_num_2):
                    max_num_2 = nums[i]
                    max_num_2_idx = i
        
        # Return highest number index if highest number >= 2nd highest number
        if(max_num_1 >= (2 * max_num_2)):
            return max_num_1_idx
        
        return -1