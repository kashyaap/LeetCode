class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # brute force way
        stack = []
        # nums = sorted(nums)
        # for i in range(len(nums)-2):
        #     for j in range(i+1, len(nums)-1):
        #         for k in range(j+1, len(nums) ):
        #             n = sorted([nums[i], nums[j],nums[k]])
        #             if nums[i] + nums[j]+ nums[k]== 0 and n not in stack :
        #                 stack.append(n)
        # return stack

        # not the brute force way
        
        # for i in range(len(nums)):
        #     target = nums[i] * -1

        #     left = i+1
        #     right = i+2
            
        #     while(left < len(nums) and right < len(nums)):
                
        #         if(nums[left]+nums[right] < target):
        #             pass
        #         elif(nums[left]+nums[right] == target):
        #             n = [nums[i], nums[left],nums[right]]
        #             if sorted(n) not in stack:
        #                 stack.append(n)
        #         if(right > len(nums)):
        #             left += 1
        #             right = left +1
        #         elif(right == len(nums)):
        #             break
        #         else:
        #             right +=1

        # return stack
        stack = []
        nums.sort()
        for i in range(len(nums)):

            if (i > 0 and nums[i] == nums[i-1]):
                continue            
            left,right = i+1, len(nums) -1
            target = -nums[i]
            
            while left < right : 
                currentSum = nums[left] + nums[right]
                if currentSum == target:
                    stack.append([nums[i],nums[left],nums[right]])
                    while(left < right and nums[left] == nums[left+1]):
                        left += 1
                    while(left < right and nums[right] == nums[right-1]):
                        right -= 1
                    left += 1
                    right -= 1
                elif currentSum > target:
                    right -= 1
                else:
                    left += 1
        return stack
