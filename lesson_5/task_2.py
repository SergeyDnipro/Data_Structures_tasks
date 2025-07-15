alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def kth_character(k: int, word: str) -> str:
    if not word:
        return ""
    if k < len(word):
        return word[k - 1]
    new_word = ''
    for letter in word:
        letter_index = alphabet.index(letter)
        new_letter = alphabet[letter_index + 1] if letter_index < len(alphabet) - 1 else alphabet[0]
        new_word += new_letter
    temp_word = word + new_word
    return kth_character(k, temp_word)

print(kth_character(6, 'ABC'))