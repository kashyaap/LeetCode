class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        counter = 1
        val = nums[0]
        while(counter < len(nums)):
            if(nums[counter] == val):
                nums.pop(counter)
            else:
                val = nums[counter]
                counter += 1
              
        print len(nums), nums
