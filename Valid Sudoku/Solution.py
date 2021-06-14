class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        hashset = set()
        
        length, width  = len(board), len(board[0])
        string  = ""
        
        for i in range(length):
            for j in range(width):
                
                if(board[i][j] != "."):
                    row_str = str(board[i][j]) + "row" +str(i)
                    col_str = str(board[i][j]) + "col" +str(j) 
                    block_str = str(board[i][j]) + "block" + str(i/3) + str(j/3)
                    
                    print(row_str)
                    print(col_str)
                    print(block_str)
                    
                    if (row_str in hashset or col_str in hashset or block_str in hashset):
                        return False
                    
                    hashset.add(row_str)
                    hashset.add(col_str)
                    hashset.add(block_str)
        return True