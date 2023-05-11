def rgb(r, g, b):
    print(r,g,b)
    min_max = lambda y: min(255, max(0, y))
    r, g, b = min_max(r), min_max(g), min_max(b)
    return format("%02x%02x%02x" % (r,g,b)).upper()
