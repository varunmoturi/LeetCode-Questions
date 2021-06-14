class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # Return "" if empty array
        if(len(strs) == 0):
            return ""
        
        # Initialize prefix to first string
        prefix = strs[0]
        
        # Loop from 2nd string to end
        for i in range(1,len(strs)):
            # Check if prefix present in word
            while(prefix != strs[i][0:len(prefix)]):
                # Decrement a character from prefix string
                prefix = prefix[:-1]
                if(prefix == ""):
                    break
        return prefix
            