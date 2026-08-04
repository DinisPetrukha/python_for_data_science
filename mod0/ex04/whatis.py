import sys

try:
	assert len(sys.argv) <= 2, "more than one argument is provided"

	if len(sys.argv) == 2:
		## try to convert the value to int inside a try/except scope
		try:
			num = int(sys.argv[1])
		except ValueError:
			# raise forces an AssertionError
			raise AssertionError("argument is not an integer")

		if num % 2 == 0:
			print("I'm Even.")
		else:
			print("I'm Odd.")



except AssertionError as msg:
    print(f"AssertionError: {msg}")