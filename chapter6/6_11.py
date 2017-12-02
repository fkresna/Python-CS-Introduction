def squareEach(nums):
	for i in range(0,len(nums)):
		nums[i] = nums[i]**2
	return nums
nums = [2,3,4,5,6,7,8,9]
print(squareEach(nums))
