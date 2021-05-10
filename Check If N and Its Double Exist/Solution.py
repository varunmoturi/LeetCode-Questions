class Solution(object):
    def checkIfExist(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        seen = set()
        
        for num in arr:
            if(num*2 in seen):
                return True
            elif(num%2 == 0 and num/2 in seen):
                return True
            else:
                seen.add(num)
            