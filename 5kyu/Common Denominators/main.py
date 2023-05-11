from math import lcm
def convert_fracts(lst):
    for x in lst:
        x[0],x[1] = int(x[0] * (lcm(*[x[1] for x in lst]) // x[1])),lcm(*[x[1] for x in lst])
    return lst
