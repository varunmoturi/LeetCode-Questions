class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left_idx = 0
        right_idx = len(numbers) - 1
        
        while(left_idx < right_idx):
            s = numbers[left_idx] + numbers[right_idx]
            
            if(s == target):
                return [left_idx+1, right_idx+1]
            elif(s < target):
                left_idx = left_idx + 1
            else:
                right_idx = right_idx - 1
                
        return [-1, -1]