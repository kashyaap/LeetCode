class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        charArray = [ord(char) for char in s]
        l = len(charArray)
        largest = []
        temp = []
        for i in range (0, l):
            ch = charArray[i]
            if ch in temp:
                if len(temp) > len(largest):
                    largest = temp
                    temp = []
                    temp.append(ch)
                else:
                    chindex = temp.index(ch)
                    shortened_list = temp[chindex +1:]
                    shortened_list.append(ch)
                    temp = shortened_list
            else:
                temp.append(ch)
                if len(temp) > len(largest):
                    largest = temp
        return(len(largest))
        
        

        
