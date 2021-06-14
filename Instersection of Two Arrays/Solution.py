class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ret_array = []
        hashset = set()
        
        for i in nums1:
            if i not in hashset:
                hashset.add(i)
        
        for i in nums2:
            if i in hashset:
                ret_array.append(i)
                hashset.remove(i)
        
        return ret_array
            