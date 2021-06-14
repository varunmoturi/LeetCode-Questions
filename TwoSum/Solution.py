class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = dict()
        
        for i in range(len(nums)):
            complement = target - nums[i]
            
            if nums[i] in hashmap:
                return [hashmap[nums[i]], i]
            else:
                hashmap[complement] = i        