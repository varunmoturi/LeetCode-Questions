class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hashmap = {}
        diff = 0
        
        for i in range(len(nums)):
            if nums[i] not in hashmap:
                hashmap[nums[i]] = i
            else:
                diff = abs(hashmap[nums[i]] - i)
                if(diff <= k):
                    return True
                else:
                    hashmap[nums[i]] = i
                    
        return False