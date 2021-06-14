class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        up      = 0
        down    = 1
        right   = 2
        left    = 3
        
        direction = right
        
        m = len(matrix)
        n = len(matrix[0])
        
        bound_right     = n - 1
        bound_left      = 0
        bound_top       = 0
        bound_bottom    = m - 1
        
        i = j = 0
        
        ret_arr = []
        
        for x in range(m * n):
            ret_arr.append(matrix[i][j])
            
            if(direction == right):
                if((j+1) <= bound_right):
                    j = j + 1
                else:
                    direction = down
                    bound_top = bound_top + 1
                    i = i + 1
                    
            elif(direction == down):
                if((i+1) <= bound_bottom):
                    i = i + 1
                else:
                    direction = left
                    bound_right = bound_right - 1
                    j = j - 1
                    
            elif(direction == left):
                if((j-1) >= bound_left):
                    j = j - 1
                else:
                    direction = up
                    bound_bottom = bound_bottom - 1
                    i = i - 1
                    
            elif(direction == up):
                if((i-1) >= bound_top):
                    i = i - 1
                else:
                    direction = right
                    bound_left = bound_left + 1
                    j = j + 1
        
        return ret_arr