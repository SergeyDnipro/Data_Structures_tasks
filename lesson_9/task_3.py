from typing import List

set1 = {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'}
set2 = {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'}
set3 = {'z', 'x', 'c', 'v', 'b', 'n', 'm'}

def find_words(words: List[str]) -> List[str]:
    result_array = []
    for word in words:
        word_in_list = set(word.lower())
        if word_in_list.issubset(set1) or word_in_list.issubset(set2) or word_in_list.issubset(set3):
            result_array.append(word)
    return result_array

print(find_words(['car', 'rex']))