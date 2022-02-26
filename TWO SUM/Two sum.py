class Solution(object):
    def twoSum(self, nums, target):
        m = dict()
        for i, x in enumerate(nums):
            if target-x in m:
                return (m[target-x], i)
            m[x]=i