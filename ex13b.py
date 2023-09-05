# repeat of Ex13 but with one more argument variable

# import argv from the sys library
from sys import argv

script, name, age, pet, petAge= argv

print(f"Hello {name}, this is the {script} script.")
print(f"I see you're {age} years old and that your pet {pet} is {petAge} years old.")

# print("Hello", name, "this is the", script, "script")
# print("I see you're", age, "years old and that your pet", pet, "is", petAge, "years old.")


