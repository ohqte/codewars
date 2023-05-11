# [Strip Comments](https://www.codewars.com/kata/51c8e37cee245da6b40000bd)

> DESCRIPTION:

Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace at the end of the line should also be stripped out.

**Example:**

Given an input string of:

```plain
apples, pears # and bananas
grapes
bananas !apples
```

The output expected would be:

```plain
apples, pears
grapes
bananas
```

The code would be called like so:

```py
result = solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"])
# result should == "apples, pears\ngrapes\nbananas"
```

> SOLUTION:

```py
def strip_comments(strs,mkers):
    a = strs.split("\n")
    for x in range(len(a)):
        for y in mkers:
            a[x] = a[x].split(y)[0].rstrip()
    return "\n".join(a)
```