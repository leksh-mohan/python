from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
print("Current date and time =", dt_string)	
print("Current year:", now.year)
print("Month of year:",now.strftime("%B"))
print("Weak number of the year:",now.strftime("%W"))
print("Weakday of the week:",now.strftime("%w"))
print("Day of year:",now.strftime("%j"))
print("Day of the month:",now.strftime("%d"))
print("Day of the week:",now.strftime("%A"))
