class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        d,p = {},{}
        for ch in s:
            d[ch] = d.get(ch, 0) + 1
        for ch in t:
            p[ch] = p.get(ch, 0) + 1
        return(d == p)
