class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        ref_idx = 0
        
        for i in range(1, len(nums)):
            if(nums[i] != nums[ref_idx]):
                nums[ref_idx + 1] = nums[i]
                ref_idx = ref_idx + 1
                
        return ref_idx + 1 