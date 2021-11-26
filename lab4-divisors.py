i = 1
number = int(input('Please enter a number: '))
while i < number:
  i += 1
  if number % i == 0:
    print(i)