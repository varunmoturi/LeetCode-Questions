class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        # Empty Array
        if(len(nums) == 0):
            return 0
        
        # Array with 1 element
        if(len(nums) == 1):
            if(nums[0] == val):
                return 0
            else:
                return 1
        
        # Array with more than 1 element
        first = 0
        last = len(nums) - 1
        
        while( first != last ):
            if(nums[last] ==  val):
                last = last - 1
                continue
                
            if(nums[first] == val):
                nums[first] = nums[last]
                nums[last] = val
                first = first + 1
                last = last - 1
                # Check if 'first' and 'last' crossed over during swap
                if(first > last):
                    return first
            else:
                first = first + 1
        
        # Case when 'first' and 'last' intersected at 'val'
        if(nums[first] == val and nums[last] == val ):
            return first
        
        # Case when all elements are 'val'
        if(first == 0 and nums[first] == val ):
            return 0
        
        return first + 1