#O(N)



def reverse_integer(n):

	reversed=0
	remainer=0

	while n>0:
		remainer=n%10
		n=n//10
		reversed=reversed*10+remainer

	return reversed

if __name__ == "__main__":

	print(reverse_integer(4321))