# [The Hashtag Generator](https://www.codewars.com/kata/52449b062fb80683ec000024)

> DESCRIPTION:

The marketing team is spending way too much time typing in hashtags.<br>
Let's help them with our own Hashtag Generator!

Here's the deal:

- It must start with a hashtag (`#`).
- All words must have their first letter capitalized.
- If the final result is longer than 140 chars it must return `false`.
- If the input or the result is an empty string it must return `false`.

**Examples**

```plain
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
```

> SOLUTION:

```py
def generate_hashtag(s):
    s = "#" + "".join([x.capitalize() for x in s.strip().split()])
    return s if(len(s) < 140 and len(s) > 1) else False
```
