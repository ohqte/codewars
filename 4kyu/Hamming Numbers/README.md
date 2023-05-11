# [Hamming Numbers](https://www.codewars.com/kata/526d84b98f428f14a60008da)

> DESCRIPTION:

A *[Hamming number](https://en.wikipedia.org/wiki/Regular_number)* is a positive integer of the form *2<sup>i</sup>3<sup>j</sup>5<sup>j</sup>*, for some non-negative integers *i*, *j*, and *k*.

Write a function that computes the *n<sup>th</sup>* smallest Hamming number.

Specifically:

- The first smallest Hamming number is 1 = 203050
- The second smallest Hamming number is 2 = 213050
- The third smallest Hamming number is 3 = 203150
- The fourth smallest Hamming number is 4 = 223050
- The fifth smallest Hamming number is 5 = 203051

The 20 smallest Hamming numbers are given in the Example test fixture.

Your code should be able to compute the first `5 000` ( LC: `400`, Clojure: `2 000`, NASM, C, D, C++, Go and Rust: `13 282` ) Hamming numbers without timing out.

> SOLUTION:

```py
def hamming(n):
    bases = [2, 3, 5]
    exps = [0, 0, 0]
    hamms = [1]
    for _ in range(1, n):
        next_hamms = [bases[i] * hamms[exps[i]] for i in range(3)]
        next_hamm = min(next_hamms)
        hamms.append(next_hamm)
        for i in range(3):
            exps[i] += int(next_hamms[i] == next_hamm)
    return hamms[-1]
```