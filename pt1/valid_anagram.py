def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t): 
            return False 
        
        counts_s = defaultdict(int)
        counts_t = defaultdict(int)

        for i, x in enumerate(s): 
            counts_s[x] += 1
            counts_t[t[i]] += 1
        
        return counts_s == counts_t

        