from itertools import permutations
char_list = ['a','e','i','o','u']
allstrings=permutations(char_list)

for string in allstrings:
    print(''.join(string))