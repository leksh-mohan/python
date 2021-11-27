dict = {}
new_str = input("Enter string:")
for n in new_str:
    if n in dict.keys():
        dict[n] += 1
    else:
        dict[n] = 1
print(dict)
