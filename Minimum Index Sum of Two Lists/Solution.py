class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        hashmap = {}
        leastIdx = sys.maxint
        s = 0
        
        ret_arr = []
        
        for i in range(len(list1)):
            hashmap[list1[i]] = i
        
        for i in range(len(list2)):
            if(list2[i] in hashmap):
                s = i + hashmap[list2[i]]
                if(s < leastIdx):
                    ret_arr = []
                    ret_arr.append(list2[i])
                    leastIdx = s
                else:
                    if(s == leastIdx):
                        ret_arr.append(list2[i])
                        
        return ret_arr