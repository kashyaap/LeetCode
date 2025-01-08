class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        elementMap = defaultdict(int)

        for i in nums:
            i = str(i)
            elementMap[i] += 1
        
        x  = list(elementMap.values())
        val_based_rev = OrderedDict(sorted(elementMap.items(), key=lambda item: item[1], reverse=True))
        
        res =[]
        for key, value in islice(val_based_rev.items(), k):
            res.append(int(key))

        return res
