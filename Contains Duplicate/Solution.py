class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        hashset = set()
        
        for i in nums:
            if i not in hashset:
                hashset.add(i)
            else:
                return True
            
        return False
        