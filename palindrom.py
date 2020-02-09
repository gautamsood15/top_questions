#O(N) 



def is_palindrom(str):
	original_str = str
	reversed_str = str[::-1]

	if original_str == reversed_str:
		return True

	return False


def is_palindrom_python(str):
	return str == ''.join(str[::-1])


if __name__ == "__main__":

	str = 'radar'
	print(is_palindrom_python(str))
