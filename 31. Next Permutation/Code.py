class Solution:
	def nextPermutation(self, nums: List[int]) -> None:
		"""
		Do not return anything, modify nums in-place instead.
		"""
		n = len(nums)
		if n == 1: return None

		i = n-1

		while i >= 1 and nums[i] <= nums[i-1]: 
			i -= 1

		j = n-1
		while j > i-1 and nums[j] <= nums[i-1]:
			j -= 1

		nums[i-1], nums[j] = nums[j], nums[i-1]

		nums[i:] = sorted(nums[i:])