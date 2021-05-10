class Solution(object):
    def duplicateZeros(self, arr):
        """
        :type arr: List[int]
        :rtype: None Do not return anything, modify arr in-place instead.
        """
        count_0 = 0
        
        #Count 0s
        for num in arr:
            if(num == 0):
                count_0 = count_0 + 1
        
        #Create empty array with extra space
        temp_arr = [0 for x in range(len(arr) + count_0)]
        
        arr_index = 0
        tmp_arr_index = 0
        
        #Loop through array
        while(tmp_arr_index < len(temp_arr)):
            if(arr[arr_index] != 0):
                temp_arr[tmp_arr_index] = arr[arr_index]
                tmp_arr_index = tmp_arr_index + 1
            else:
                temp_arr[tmp_arr_index] = arr[arr_index]
                temp_arr[tmp_arr_index + 1] = 0
                tmp_arr_index = tmp_arr_index + 2
            arr_index = arr_index + 1
            
        for i in range(len(arr)):
            arr[i] = temp_arr[i]