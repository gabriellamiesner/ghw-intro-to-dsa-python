def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]

        given: numbers array, sorted in increasing order
        do: loop thru the numbers array, find the indices of the 2 integers that = target together 
            - then add one to both index and return in an array 

        create our pointers 

        create our while loop 

            - curr_sum = nums[l] + nums[r]
            - if target == curr_sum, return our indices + 1
            - elif target > curr_sum: increment left up 
            - else: r -= 1


        1d v 2d /// 0-indexed, 1-indexed 
        """

        l = 0 
        r = len(numbers) - 1

        while l < r: 
            curr_sum = numbers[l] + numbers[r]
            if target == curr_sum: 
                return [l+1, r+1]
            elif target > curr_sum: 
                l +=1
            else: 
                r -= 1
        
        