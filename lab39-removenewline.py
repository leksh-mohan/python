flist = open("test.txt").readlines()
print([s.rstrip('\n') for s in flist])