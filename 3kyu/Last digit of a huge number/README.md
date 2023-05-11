## [Last digit of a huge number](https://www.codewars.com/kata/5518a860a73e708c0a000027)


> DESCRIPTION:
For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.

This kata generalizes Last digit of a large number; you may find useful to solve it beforehand.

> SOLUTION:


```py
def last_digit(nums):

    res = 1
    if not nums:
        return res
    else:

        for x in nums[len(nums):0:-1]:
            res = pow(x, res)

            if res > 2:
                res = (res - 2) % 4 + 2

    return nums[0] ** res % 10
```