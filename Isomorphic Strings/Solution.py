class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s_hash = {}
        t_hash = {}
        s_val = ''
        t_val = ''
        for i in range(len(s)):
            s_val = s[i]
            t_val = t[i]
            
            if s_val not in s_hash:
                s_hash[s_val] = t_val
            else:
                if(s_hash[s_val] != t_val):
                    return False
            
            if t_val not in t_hash:
                t_hash[t_val] = s_val
            else:
                if(t_hash[t_val] != s_val):
                    return False
            
        return True