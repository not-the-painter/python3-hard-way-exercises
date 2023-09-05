# import argv from the sys library
from sys import argv

script, user_name = argv
prompt = '> '

print(f"Hi {user_name}! I'm the {script} script!")

print("How old are you?")
age = input(prompt)

print("Where do you live?")
city = input(prompt)

print("What do you do?")
occupation = input(prompt)

print(f"""
So {user_name}, you're {age} years old, you live in {city}. 
You're a {occupation}. That's cool!
Am I in {city} now?
""")
