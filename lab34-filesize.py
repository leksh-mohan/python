import os
statinfo = os.stat("test.txt")
print("File size",statinfo.st_size) 
