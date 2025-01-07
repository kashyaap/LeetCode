class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        # def checkAnagram(anaStr, ifAna):
        #     return sorted(anaStr) == sorted(ifAna)

        # strs = sorted(strs)
        # op = [[strs[0]]]
        # for i in range( 1, len(strs)):
        #     for j in range(0, len(op)):
        #         if(checkAnagram(strs[i], op[j][0])):
        #             op[j].append(strs[i])
        #             break
        #         if(j == len(op)-1):
        #             op.append([strs[i]])
        #             break
        # return op

        anagram_map = defaultdict(list)
        
        for s in strs:
            sorted_key = "".join(sorted(s))
            anagram_map[sorted_key].append(s)
        
        return list(anagram_map.values())

        
        
