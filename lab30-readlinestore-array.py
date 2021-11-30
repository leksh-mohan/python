file_array = []
with open("test.txt") as f:
    for line in f:
        file_array.append(line)
print(file_array)
