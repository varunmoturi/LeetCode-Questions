class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        
        a_bin = int(a[i])
        b_bin = int(b[j])
        carry = 0
        s = 0
        
        ret_str = ''
        
        for x in range(max(len(a),len(b))):
            s = carry + a_bin + b_bin
            
            if(s == 2):
                ret_str = '0' + ret_str
                carry = 1
            elif(s == 3):
                ret_str = '1' + ret_str
                carry = 1
            else:
                ret_str = str(s) + ret_str
                carry = 0
            
            i,j = i-1, j-1
            
            a_bin = 0 if(i<0) else int(a[i])
            b_bin = 0 if(j<0) else int(b[j])
            
        if(carry == 1):
            ret_str = '1' + ret_str
        
        return ret_str