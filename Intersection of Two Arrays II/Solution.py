class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        hashmap     = {}
        ret_arr     = []
        
        short_arr   = []
        long_arr    = []
        
        if(len(nums1) < len(nums2)):
            short_arr   = nums1
            long_arr    = nums2
        else:
            short_arr   = nums2
            long_arr    = nums1

        for i in range(len(short_arr)):
            if short_arr[i] not in hashmap:
                hashmap[short_arr[i]] = 1
            else:
                hashmap[short_arr[i]] = hashmap[short_arr[i]] + 1
        
        for i in range(len(long_arr)):
            if long_arr[i] in hashmap:
                if(hashmap[long_arr[i]] != 0):
                    ret_arr.append(long_arr[i])
                    hashmap[long_arr[i]] = hashmap[long_arr[i]] - 1
        
        return ret_arr