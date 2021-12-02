my_list = []
num = int(input('How many numbers: '))
for n in range(num):
    numbers = int(input('Enter number '))
    my_list.append(numbers)
print("Sum of a list of numbers :", sum(my_list))
