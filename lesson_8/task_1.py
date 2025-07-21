def is_valid(s: str) -> bool:
    if not s:
        return True
    stack = []
    for symbol in s:
        if symbol in hash_table.keys():
            stack.append(symbol)
        elif stack and symbol in hash_table.values():
            prev_symbol = stack.pop()
            if hash_table[prev_symbol] != symbol:
                return False
        else:
            return False

    if stack:
        return False
    return True

hash_table = {
    '[':']',
    '{':'}',
    '(':')',
}
