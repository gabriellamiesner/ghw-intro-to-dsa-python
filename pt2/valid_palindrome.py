def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool

        given: string 
        do: check if palindrome, return t/f depending on results 
            1. convert all letters to lowercase ✅
            2. remove all non-alphanumeric chars (only numbers and letters in our string)
            3. forwards == backwards of our string 

        s = s.lower()
        replace all whitespace with NO space 

        left pointer and right pointer 0, end of our list 

        while loop - while l < r 
        - if/elif string at l or right pointer isnotalphanumeric, increment or decrement by one
        - if string at l and string at r are ==, increment up by one and decrement down by one
        - else: return False 
        
        once while loop has executed fully, we will return true 
        """

        s = s.lower()
        s = s.replace(' ', '')

        l = 0 
        r = len(s) -1 

        while l < r: 
            if not s[l].isalnum(): 
                l += 1
            elif not s[r].isalnum(): 
                r -= 1
            elif s[r] == s[l]: 
                l += 1
                r -= 1
            else: 
                return False 
        return True
        