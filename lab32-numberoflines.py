num_lines = 0
with open("test.txt") as f:
    for line in f:
        num_lines += 1
print(num_lines)
