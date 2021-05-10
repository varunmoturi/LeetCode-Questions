class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        # Initilaize Indexes
        nums1_left_idx = m - 1
        nums1_right_idx = m + n - 1
        nums2_idx = n - 1
        
        # Merge in Reverse Order
        while((nums2_idx != -1) and (nums1_left_idx != -1)):
            if( nums2[nums2_idx] >= nums1[nums1_left_idx] ):
                nums1[nums1_right_idx] = nums2[nums2_idx]
                nums2_idx =  nums2_idx - 1
            else:
                nums1[nums1_right_idx] = nums1[nums1_left_idx]
                nums1_left_idx =  nums1_left_idx - 1
                
            nums1_right_idx =  nums1_right_idx - 1
        
        # Fill remaining elements of nums2 in nums1 
        while(nums2_idx > -1):
            nums1[nums1_right_idx] = nums2[nums2_idx]
            nums1_right_idx =  nums1_right_idx - 1
            nums2_idx =  nums2_idx - 1