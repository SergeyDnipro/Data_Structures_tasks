# def decode(s: str):
#     list_str = list(s)
#     temp_letter = ""
#     if s[0].isdigit():
#         return str(int(s[0]) * decode(s[1:]))
#     elif s[0] == '[':
#         for letter in s[1:]:
#             if letter.isalpha():
#                 temp_letter += letter
#             elif letter == ']':
#                 return

def decode(s: str):
    list_str = list(s)
    char = 0
    k = 1
    stack = []

    while char <= len(list_str) - 1:
        if list_str[char].isdigit():
            k = int(list_str[char])
            char += 1
            if list_str[char] == '[':
                temp_letter = ""
                while char <= len(list_str) - 1:
                    char += 1
                    if list_str[char].isalpha():
                        temp_letter += list_str[char]
                    elif list_str[char] == ']':
                        stack.append(k * temp_letter)
                        char += 1
                        break

    print(''.join(stack))

print(decode('3[a]2[bc]'))
print(decode('3[a2[c]]'))