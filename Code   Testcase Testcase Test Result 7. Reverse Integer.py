class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        # String approach not working 
        # if( x < 1534236469 and x > -1563847412):
        #     x_string = str(x)
        #     to = False
        #     if (x_string[0] == '-'):
        #         x_string = '' + x_string[1:]
        #         to=True

        #     z = int(x_string[::-1])
        #     if (to):
        #         return (z*(-1))
        #     else:
        #         return z
        # else:
        #     return 0

        def reverse_int(n):
            reverse = 0
            c =0
            while(n!= 0):
                reverse = (n%10) + (reverse*10)
                n = n/10
            if reverse < -2147483648 or reverse > 2147483648:
                return 0
            else:
                return reverse
        if(x>0 ):
            return(reverse_int(x))
        else:
            x=x*-1
            return(-1*reverse_int(x))

        
