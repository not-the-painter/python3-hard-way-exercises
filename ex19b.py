# define a function and try to find 10 different ways to call it

# a simple function that adds two numbers passed to it
from sys import argv

def add_nums(arg1, arg2):
	nums_sum = arg1 + arg2
	return(nums_sum)

#1
print("1. Pass argument variables from the command line when running the script:")
script, num1, num2 = argv
result = add_nums(int(num1), int(num2))
print(result)

# 2
print("2. Pass numbers directly:")
result = add_nums(2, 4)
print(result)

# 3
print("3. Pass variables from the script:")
first_num, second_num = 3, 5
result = add_nums(first_num, second_num)
print(result)

# 4
print("4. Pass results of math calculation:")
result = add_nums(3*4**2, (6+2)*4)
print(result)

# 5 
print("5. Pass a combination of math & variables:")
result = add_nums(first_num * 3, second_num - first_num)
print(result)

# 6
print("6. Pass user input:")
first_num = int(input("first number: "))
second_num = int(input("second number: "))
result = add_nums(first_num, second_num)
print(result)



	