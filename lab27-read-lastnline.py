#n is number of lines
n=2
f = open("test.txt", "r")
lines = f.readlines()
last_lines = lines[-n:]
print(last_lines)
