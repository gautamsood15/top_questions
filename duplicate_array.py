#o(N)
# In place algorithms

def duplicates(nums):

	for num in nums:
		if nums[abs(num)] >= 0:
			nums[abs(num)] = -nums[abs(num)]
		else:	
			print("Repitition found: ", abs(num))


if __name__ == "__main__":

	a = [2, 6, 5, 3, 4, 3, 2]

	duplicates(a)