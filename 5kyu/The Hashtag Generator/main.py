def generate_hashtag(s):
    s = "#" + "".join([x.capitalize() for x in s.strip().split()])
    return s if(len(s) < 140 and len(s) > 1) else False
