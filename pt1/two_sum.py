def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        numeros = []

        for i, x in enumerate(nums): 
            difference = target - x
            if difference in nums and nums.index(difference) in numeros: 
                return [i, nums.index(difference)]
            else: 
                numeros.append(i)
        