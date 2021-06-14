class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        n = len(s)
        result = ""
            
        w_start = w_end = 0
        
        while(w_start < n and w_end < n):
            
            while(w_start<=n-1 and s[w_start] == ' '):
                w_start = w_start + 1
                
            w_end = w_start
            
            while(w_end<=n-1 and s[w_end] != ' '):
                print(w_end)
                w_end = w_end + 1
            
            if(w_start != n):
                result = (s[w_start:w_end]) if (result == "") else (s[w_start:w_end] + " " + result)
            
            w_start = w_end

        return result