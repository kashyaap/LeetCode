class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        val = nums[0]
        pointer = 1
        k =1
        no_count = 1
        while(pointer < len(nums)):
            if(nums[pointer] == val ):
                if(no_count <2 ):
                    nums[k] = val 
                    k += 1
                    no_count += 1
                    pointer += 1
                else:
                    pointer += 1
            else:
                nums[k] = nums[pointer]
                val = nums[pointer]
                k += 1 
                pointer += 1
                no_count = 1
        
        nums = nums[0:k]
        return k
