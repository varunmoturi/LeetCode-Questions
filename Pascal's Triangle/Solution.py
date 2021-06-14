class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        ret_arr = []
        tmp_list = []
        prev_list = []
        
        i = j = 0
        
        while(i < numRows):
            # Each row will contain (i+1) elements
            if(j < (i+1)):
                if(j == 0 or j == i):
                    # First and the last elements in each row will be 1
                    tmp_list.append(1)
                else:
                    # sum of 2 numbers directly above current number
                    tmp_list.append(prev_list[j] + prev_list[j-1]) 
                j = j + 1
            
            # Increment row, reset column store prev_row data and append to final list
            # If end of column reached
            if(j >= (i+1)):
                ret_arr.append(tmp_list)
                prev_list = tmp_list
                tmp_list = []
                i = i + 1
                j = 0
                
        return ret_arr