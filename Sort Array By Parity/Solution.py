class Solution(object):
    def sortArrayByParity(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        l = 0
        r = len(A) - 1
        
        while(r > l):
            if(A[l]%2 != 0 and A[r]%2 == 0):
                tmp  = A[l]
                A[l] = A[r]
                A[r] = tmp
            
            if(A[l]%2 == 0):
                l = l + 1
                
            if(A[r]%2 != 0):
                r = r - 1
        
        return A