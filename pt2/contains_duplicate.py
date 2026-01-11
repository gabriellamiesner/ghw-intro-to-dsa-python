def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        given: array of numbers 
        do: return True if multiple of same int, return False otherwise

        --- create an array - house the ints we've already seen ---
        1. sort our nums array 
        2. loop thru our nums array (start at index 1)
        3. if curr_int == prev_int - return True 
        4. else: continue 
        5. if the entire for loop executes, we will return false 
        """

        # seen = []
        # nums.sort()
        # for i, x in enumerate(nums): 
            # first attempt: did not pass 
            # if i in seen: 
            #     return True 
            # else: 
            #     seen.append(i)

            # second attempt: did pass
            # if i == 0: 
            #     continue 
            # elif x == nums[i-1]: 
            #     return True 
            # else: 
            #     continue 
        # return False 


        return len(nums) != len(set(nums))

        




        