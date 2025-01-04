class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """   
        # l = 0 
        largest = ""
        # while(l < len(s)):
        #     for cursor in range(0,len(s)):
        #         if(s[cursor] == s[l]):
        #             res = s[l:cursor+1][::-1] == s[l:cursor+1]
        #             if(res):
        #                 if len(largest) < len(s[l:cursor+1]):
        #                     largest = s[l:cursor+1]
        #     l+= 1

        # return largest

        # Expand around the center aproach 
        def expand_around_center( left , right, s):
            while(left >= 0 and right  < len(s) and s[left] == s[right]):
                left -= 1
                right +=1
            return s[left+1:right]

        for i in range(len(s)):
            odd_center = expand_around_center(i,i,s)
            even_center = expand_around_center(i,i+1, s)

            if len(odd_center) >len(largest):
                largest = odd_center
            if len(even_center) > len(largest):
                largest = even_center
        return largest
        
    
