# The goal of this exercise is to convert a string to a new 
# string where each character in the new string is "(" if that 
# character appears only once in the original string, or ")" if 
# that character appears more than once in the original string. 
# Ignore capitalization when determining if a character is a 
# duplicate.

#EXAMPLE:
# "din"      =>  "((("
#"recede"   =>  "()()()"
#"Success"  =>  ")())())"
#"(( @"     =>  "))((" 


def duplicate_encode(word):
    string = ""
    my_dict = {}
    for letter in word.lower():
        if letter not in my_dict:
            my_dict[letter] = 0
        my_dict[letter] += 1
    for letter in word.lower():
        if letter in my_dict and my_dict[letter] > 1:
            string += ")"
        else:
            string += "("
    return string