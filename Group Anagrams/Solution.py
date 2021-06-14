class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # Sort each word in the list
        sorted_list = []
        for word in strs:
            sorted_list.append(''.join(sorted(word)))
        
        # Create Hashmap with key = sorted_word, value = list of unsorted words associated witht the sorted word 
        hashmap = {}
        for i in range(len(sorted_list)):
            if sorted_list[i] not in hashmap:
                hashmap[sorted_list[i]] = [strs[i]]
            else:
                hashmap[sorted_list[i]].append(strs[i])
        
        # Create a list from each key created
        ret_arr = []
        for i in range(len(hashmap.keys())):
            ret_arr.append(hashmap[hashmap.keys()[i]])
        
        return ret_arr