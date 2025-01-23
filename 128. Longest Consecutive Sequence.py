class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        numset = set(nums)
        longest = 0

        for num in numset:
            if(num - 1 not in numset):
                length = 0 
                while(num in numset):
                    length += 1
                    num += 1
                
                if(longest < length ):
                    longest = length
        return longest
