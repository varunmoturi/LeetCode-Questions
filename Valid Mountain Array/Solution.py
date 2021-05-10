class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        
        #Case when there are less than 3 elements in the list
        if(len(arr) < 3):
            return False
        
        inc_flag = True
        
        inc_count = 0
        dec_count = 0
        
        for i in range(len(arr) - 1):
            # Increasing Order
            if(inc_flag):
                if(arr[i+1] < arr[i]):
                    dec_count = dec_count + 1
                    inc_flag = False
                elif(arr[i+1] > arr[i]):
                    inc_count = inc_count + 1
                else:
                    return False
            # Decreasing Order
            else:
                if(arr[i+1] >= arr[i]):
                    return False
                else:
                    dec_count = dec_count + 1
        
        if(inc_count > 0 and dec_count > 0):        
            return True
        else:
            return False