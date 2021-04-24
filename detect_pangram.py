import string

def is_pangram(s):
    sentence = s.lower()
    listing = ""
    for letter in string.ascii_letters:
        for i in range(len(sentence)):
            if letter == sentence[i] and letter not in listing:
                listing += letter
    print(listing)
    if listing == string.ascii_lowercase:
        return True
    else:
        return False