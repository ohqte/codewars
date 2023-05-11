def valid_parentheses(string):
    front = back = 0
    for x in list(string):
        match x:
            case "(":
                front +=1
            case ")":
                back+=1
        if (front < back):
            return False
    if front != back:
        return False
    return True
