class Solution(object):
    # def removeDuplicates(self, nums):
    #     """
    #     :type nums: List[int]
    #     :rtype: int
    #     """
    #     counter = 1
    #     val = nums[0]
    #     while(counter < len(nums)):
    #         if(nums[counter] == val):
    #             nums.pop(counter)
    #         else:
    #             val = nums[counter]
    #             counter += 1
              
    #     print len(nums), nums

    # Faster than POP solution
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pointer = 0
        k =1
        val = nums[0]

        while(pointer < len(nums)):
            if(val == nums[pointer]):
                pointer += 1
            else:
                nums[k] = nums[pointer]
                val = nums[pointer]
                pointer += 1
                k +=1 
                
        nums = nums[0:k]

        return k

