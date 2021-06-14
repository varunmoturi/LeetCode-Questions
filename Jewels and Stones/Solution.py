class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        hashset = set()
        count = 0
        
        for jewel in jewels:
            if jewel not in hashset:
                hashset.add(jewel)
        
        for stone in stones:
            if stone in hashset:
                count += 1
        
        return count