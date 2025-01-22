class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        product = 1
        zero_count = 0

        for num in nums:
            if num == 0:
                zero_count += 1
            else:
                product *= num

        for i in range(len(nums)):
            if nums[i] == 0:
                if zero_count == 1: 
                    nums[i] = product
                else:  
                    nums[i] = 0
            else:
                if zero_count > 0: 
                    nums[i] = 0
                else: 
                    nums[i] = product // nums[i]

        return nums
        


