def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s= s.lower()
        s= s.replace(' ', '')

        l = 0 
        r = len(s) - 1

        while l < r: 
            if s[l].isalnum() == False: 
                l += 1
            elif s[r].isalnum() == False: 
                r -= 1
            elif s[l] == s[r]: 
                l +=1
                r -= 1
            else: 
                return False 
        return True
            
        