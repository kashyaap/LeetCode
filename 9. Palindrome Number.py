class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        formedNo = 0
        t = x
        while(x>0):
            formedNo = x%10 + (formedNo)*10
            x= x/10

        return(t==formedNo)

