class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        hashset = set()
        cur_num = n
        
        while(True):
            res = self.getDigitSquaredSum(cur_num)
            if (res == 1):
                return True
            else:
                if(res not in hashset):
                    hashset.add(res)
                    cur_num = res
                else:
                    return False
    
    def getDigitSquaredSum(self, num):
        s = 0
        temp_num = num 
        while(temp_num != 0):
            s = s + ((temp_num % 10) * (temp_num % 10))
            temp_num = temp_num / 10

        return s
    