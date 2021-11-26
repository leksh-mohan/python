
from datetime import date
today = date.today() 

username = input("Enter username:")
age = int(input("Enter age:"))
extra_years=100-age
hundred_year=today.year+extra_years
print("Hello "+username+", ""You will turn 100 years old in "+str(hundred_year))