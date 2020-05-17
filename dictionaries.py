string_to_dictionary_file = open("dictionary_file","r")

content = string_to_dictionary_file.read()
print(content)


dict_words = content.split(' ')
counts = dict()
for word in dict_words:
    if word in dict_words:
        counts[word] += 1
    else:
        counts[word] = 1

    print(counts)
