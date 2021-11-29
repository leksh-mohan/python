given_list = [1, 2, 3]
from itertools import combinations
subs = []
for i in range(0, len(given_list)+1):
    temp = [list(x) for x in combinations(given_list, i)]
    if len(temp)>0:
        subs.extend(temp)
print(subs)

