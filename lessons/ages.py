"""Example memory diagram program."""

age: int = int(input("How old are you? "))
year: int = int(input("What year is it? "))
age_in_2041: int = 2041 - year + age
print("In 2041, you'll be " + str(age_in_2041))

age = age + 1
year = year + 1
print("In " + str(year) + ", you'll be " + str(age))

age = age + 20
year = year + 20
print("In " + str(year) + ", you'll be " + str(age))

age = age + 50
year = year + 50
print("In " + str(year) + ",you'll be " + str(age))
