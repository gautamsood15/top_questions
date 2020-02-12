#O(N)

def kadane_algorithm(nums):
	max_current = 0
	max_global = 0

	for i in range(0,len(nums)):

		max_current = max(nums[i], nums[i]+ max_current)

		if max_global < max_current:
			max_global = max_current

	return max_global

if __name__ == "__main__":

	nums = [1, -2, 3, 4, -5, 8]

	print(kadane_algorithm(nums))




