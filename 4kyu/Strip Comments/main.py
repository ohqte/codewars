def strip_comments(strs,mkers):
    a = strs.split("\n")
    for x in range(len(a)):
        for y in mkers:
            a[x] = a[x].split(y)[0].rstrip()
    return "\n".join(a)
