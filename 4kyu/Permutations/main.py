from itertools import permutations as perms
def permutations(s):
    a = [x for x in perms(s)]
    a = ["".join(x) for x in a]
    return list(set(a))
