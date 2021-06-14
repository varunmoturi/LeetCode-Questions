class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        result = ""
        w_start = w_end = 0
        n = len(s)
        
        while(w_start < n and w_end < n):
            
            while(w_start < n and s[w_start]==" "):
                w_start = w_start + 1
                
            w_end = w_start
            
            while(w_end < n and s[w_end]!=" "):
                w_end = w_end + 1
            
            if(w_start != n):
                if (result == ""):
                    result = self.reverse_str(s, w_start, w_end-1)
                else:
                    result = result + " " + self.reverse_str(s, w_start, w_end-1)  
            
            w_start = w_end
        return result
            
        
    def reverse_str(self, string, l, r):
        result = ""
        idx = r
        for i in range(r-l+1):
            result = result + string[idx]
            idx = idx - 1
        
        return result
            