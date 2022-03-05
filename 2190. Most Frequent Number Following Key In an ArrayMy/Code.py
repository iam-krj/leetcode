class Solution:
    def mostFrequent(self, nums: List[int], key: int) -> int:
        firstcount  = 0
        target=0
        secondcount= 0
        final = {}
        for i in range(len(nums) - 1):
            if nums[i] ==key:
                target = nums[i+1]
                firstcount = 0
                for k in range(len(nums)-1):
                    if nums[k]==key and nums[k+1]==target:
                        firstcount = firstcount+1
                        final[target] = firstcount
        maxi = max(final, key = final.get)
        return maxi
                        