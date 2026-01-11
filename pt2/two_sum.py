def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]


        given: nums list, target int 
        do: find the two ints in nums that = target, return indices of those int

        1. create a dictionary to hold (curr_int: index of curr_int) - 2 : 0 
        2. loop thru nums
        3. if target - curr_int in dictionary, return [curr_int_index, dictionary[difference]]
        4. else: append curr_int: index of curr_int into dictionary 
        """

        indices = {}

        for i, x in enumerate(nums): 
            difference = target - x
            if difference in indices: 
                return [i, indices[difference]]
            else: 
                indices[x] = i 
            
        