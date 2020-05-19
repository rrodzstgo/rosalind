string_to_dictionary_file = open("dictionary_file","r")

content = string_to_dictionary_file.read()

dict_words = content.split(' ')

from collections import Counter

counted_dictionary = Counter(dict_words)

for key, entry in counted_dictionary.items():
    print(key)
    print(entry)

