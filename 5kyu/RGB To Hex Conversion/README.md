# [RGB To Hex Conversion](https://www.codewars.com/kata/513e08acc600c94f01000001)

> DESCRIPTION:

The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

The following are examples of expected output values:

```py
rgb(255, 255, 255) # returns FFFFFF
rgb(255, 255, 300) # returns FFFFFF
rgb(0,0,0) # returns 000000
rgb(148, 0, 211) # returns 9400D3
```

> SOLUTION:

```py
def rgb(r, g, b):
    print(r,g,b)
    min_max = lambda y: min(255, max(0, y))
    r, g, b = min_max(r), min_max(g), min_max(b)
    return format("%02x%02x%02x" % (r,g,b)).upper()
```