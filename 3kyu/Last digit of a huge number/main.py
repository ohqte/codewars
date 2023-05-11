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