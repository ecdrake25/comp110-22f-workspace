"""Demonstrates asking the user for input."""

user_name: str = input("What is your name? ")
age: int = int(input("How old are you? "))
year: int = int(input("What year is it? "))
age_in_2050: int = 2050 - year + age

print("Hello, " + user_name + ", good morning!")
print("You are awesome, " + user_name)
print("So beautiful and young at the age of " + str(age) + " years old!")
print("You will be " + str(age_in_2050) + " years old" + " in 2050" )