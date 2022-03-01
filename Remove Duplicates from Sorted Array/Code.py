class Solution(object):
    def removeDuplicates(self, nums):
        c = 0
        for i in range(len(nums)):
            if nums[c]!= nums[i]:
                c+=1
                nums[c]=nums[i]
        return c+1
        