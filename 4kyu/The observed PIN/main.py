import itertools


def get_pins(*pwd):

    adj_keypad = {
        "1": ["1", "2", "4"],
        "2": ["2", "1", "3", "5"],
        "3": ["3", "2", "6"],
        "4": ["4", "5", "1", "7"],
        "5": ["5", "4", "6", "2", "8"],
        "6": ["6", "5", "3", "9"],
        "7": ["7", "8", "4"],
        "8": ["8", "7", "9", "5", "0"],
        "9": ["9", "8", "6"],
        "0": ["0", "8"],
    }
    pwd_comb = [
        "".join(x)
        for x in list(
            itertools.product(
                *[
                    adj_keypad[x]
                    for x in [str(x) for x in [int(x) for x in str(pwd[0])]]
                ]
            )
        )
    ]

    return pwd_comb
