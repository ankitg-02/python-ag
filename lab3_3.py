#permutation
from itertools import permutations
s=str(input("enter a string:"))
perms = [''.join(p) for p in permutations(str(s))]
print(perms)
