 def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool

        recieving: 2 strings 
        looking for: true/false our strings are an anagram (will be returned, not printed)

        steps: 
        1. create 2 dictionaries (house the counts of all the characters in our strings)
            t_dictionary 
            s_dictionary 
        2. check if length of s and t are =, if not return false 
        3. if =, for loop (len of s + t): 
            if s[i] in dictionary: increment, otherwise, append s[i] : 1 into our dictionary 
            .. for t 
        4. sort both dictionaries 
        5. return s_dictionary == t_dictionary
        """
        
        if len(s) != len(t): 
            return False 
                    
        t_dictionary = {}
        s_dictionary = {}

        for i in range(len(s)): 
            if s[i] in s_dictionary: 
                s_dictionary[s[i]] += 1
            else: 
                s_dictionary[s[i]] = 1
            
            if t[i] in t_dictionary: 
                t_dictionary[t[i]] += 1
            else: 
                t_dictionary[t[i]] = 1

        return t_dictionary == s_dictionary
            