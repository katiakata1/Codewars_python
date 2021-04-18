def spin_words(sentence):
    strings = sentence.split()
    words = []
    for string in strings:
        if len(string) < 5:
            words.append(string)
        else:
            new_list = []
            for index in range(len(string)):
                new_list.append(string[len(string)- 1 - index])
            reversed_word = ''.join(new_list)
            words.append(reversed_word)
    new_sentence = ' '.join(words)
    print(new_sentence)
    return new_sentence

x = spin_words("Hey fellow warriors")
print(x)

