class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        
        # Concat all digits and Convert to String
        num_str = ''
        for i in range(len(digits)):
            num_str = num_str + str(digits[i])
        
        # Convert to Integer, add 1 and convert back to String
        num_plus_1_str = str(int(num_str) + 1)
        
        # Append String elemnts to new array
        ret_arr = []
        for i in range(len(num_plus_1_str)):
            ret_arr.append(num_plus_1_str[i])
            
        return ret_arr