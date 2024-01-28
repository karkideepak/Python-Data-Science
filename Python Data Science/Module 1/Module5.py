# A simple function
def fun():
	print("Welcome here")

# calling the function
fun()

# Function with parameters
def add(num1:int, num2:int):
	# add two numbers
	num3 = num1 + num2
	return num3

def add(num1: int, num2: int) -> int:
	"""Add two numbers"""
	num3 = num1 + num2

	return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")


# some more functions
def is_prime(n):
	if n in [2, 3]:
		return True
	if (n == 1) or (n % 2 == 0):
		return False
	r = 3
	while r * r <= n:
		if n % r == 0:
			return False
		r += 2
	return True
print(is_prime(78), is_prime(79))
