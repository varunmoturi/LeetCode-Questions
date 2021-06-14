class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        
        n = len(nums)
        k = (k % n)
        
        # Reverse [0:n-k-1]
        self.reverseArray(nums, 0, (n-k-1))
        
        # Reverse [n-k:n-1]
        self.reverseArray(nums, (n-k), (n-1))
        
        #Reverse [0:n-1]
        self.reverseArray(nums, 0, n-1)
        
    def reverseArray(self, nums, l, r):
        while(l < r):
            temp    = nums[l]
            nums[l] = nums[r]
            nums[r] = temp
            
            l += 1
            r -= 1