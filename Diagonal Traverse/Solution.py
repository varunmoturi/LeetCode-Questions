class Solution(object):
    def findDiagonalOrder(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[int]
        """
        
        # Initialize Directions
        up = 1
        down = 0
        
        direction = up
        
        # Initialize length and width of matrix
        m = len(mat)
        n = len(mat[0])
        
        i = j = 0                       # Iterators
        ret_arr = []                    # Return Matrix
        
        for x in range(m * n):
            ret_arr.append(mat[i][j])   # Append to Retrun Matrix
            
            if(direction == up):
                if((i-1) >= 0 and (j+1) < n):   # Check edge conditions
                    i = i - 1
                    j = j + 1
                else:                           # Change direction and update iterators 
                    direction = down
                    if((j+1) < n):
                        j = j + 1
                    else:
                        i = i + 1
            else:
                if((i+1) < m and (j-1) >= 0):   # Check edge conditions
                    i = i + 1
                    j = j - 1
                else:                           # Change direction and update iterators
                    direction = up
                    if((i+1) < m):
                        i = i + 1
                    else:
                        j = j + 1
        
        return ret_arr