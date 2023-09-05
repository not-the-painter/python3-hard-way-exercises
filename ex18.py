# introducing functions
# functions basically do three things:
# 1. they name chunks of code the way variables name strings and numbers
# 2. they take arguments the way scripts take argv
# 3. using 1 and 2 they let you make "mini-scripts" or "tiny commands"

def print_two(*args):
	arg1, arg2 = args
	print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that *args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
	print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes just one argument
def print_one(arg1):
	print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
	print("I got nothin'")

print_two("Zed", "Shaw")
print_two_again("Bob", "Ross")
print_one("First!")
print_none()

