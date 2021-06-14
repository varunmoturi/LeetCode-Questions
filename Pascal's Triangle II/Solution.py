class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        prev_list = []
        curr_list = []
        i = j = 0
        
        while(i < rowIndex+1):
            if(j == 0 or j == i):
                curr_list.append(1)
                
                if(j == i):
                    prev_list = curr_list
                    curr_list = []
                    i = i + 1
                    j = 0
                else:
                    j = j + 1
            else:
                curr_list.append(prev_list[j] + prev_list[j-1])
                j = j + 1
        
        return prev_list