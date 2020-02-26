"""
Strategy: keep 2 pointers (i,j)
i tracks the baseline value
j moves forward to compare back to nums[i]
if nums[i] != nums[j] => increment i and set nums[i] to nums[j]
=> To get the length of the final array, this is i + 1 (last element index + 1 is length of full array)
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        if not nums:
            return 0
        else:
            for j in range(1,len(nums)):
                if nums[i] != nums[j]:
                    i += 1
                    nums[i] = nums[j]
        return i+1
        