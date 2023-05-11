def zeros(n):
    pow,sum = 1,0
    while (n//(5**pow) != 0):
        sum+=(n//(5**pow))
        pow+=1
    return sum
