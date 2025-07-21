from collections import defaultdict

def is_isomorphic(s: str, t: str) -> bool:
    if not s and not t:
        return True
    elif (not s or not t) or (len(s) != len(t)):
        return False

    d1 = defaultdict(int)
    list_len = len(s)
    for index in range(list_len):
        if not d1[s[index]] and t[index] in d1.values():
            return False
        elif not d1[s[index]]:
            d1[s[index]] = t[index]
        if d1[s[index]] != t[index]:
            return False
    return True

print(is_isomorphic("as", "qw"))
