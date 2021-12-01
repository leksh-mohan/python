fileHandle = open('test.txt', "r")
texts = fileHandle.readlines()
fileHandle.close()

fileHandle = open('abc.txt', "w")
for s in texts:
    fileHandle.write(s)
fileHandle.close()