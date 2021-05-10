class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        
        last_idx = len(arr) - 2                     # Point to 'last - 1' element
        max_num = arr[len(arr) - 1]                 # Initialize to last element
        curr_val = 0                                # Variable to store value in current index                                 
        # Loop from end
        while(last_idx >= 0):
            curr_val = arr[last_idx]                # Store value in current index
            arr[last_idx] = max_num                 # Replace curr_index with max_num
            max_num = max(curr_val, max_num)        # Update max_num
            last_idx = last_idx - 1                 # Decrement last_idx
        arr[-1] = -1    
        return arr