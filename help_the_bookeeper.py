# You will be given a stocklist (e.g. : L) and a list of categories in capital letters e.g :
# M = {"A", "B", "C", "W"} 
# or
# M = ["A", "B", "C", "W"] or ...
# and your task is to find all the books of L with codes belonging to each category of M and to sum their quantity according to each category.
# For the lists L and M of example you have to return the string (in Haskell/Clojure/Racket/Prolog a list of pairs):
# (A : 20) - (B : 114) - (C : 50) - (W : 0)
# where A, B, C, W are the categories, 20 is the sum of the unique book of category A, 114 the sum corresponding to "BKWRK" and "BTSQZ", 50 corresponding to "CDXEF" and 0 to category 'W' since there are no code beginning with W.
# If L or M are empty return string is "" (Clojure/Racket/Prolog should return an empty array/list instead).

def stock_list(list_of_art, list_of_cat):
    dict = {}
    string = ''
    for c in list_of_cat:
        dict[c] = 0
    
    for c in list_of_cat:
        for b in list_of_art:
            if c == b[0]:
                new = b.split(" ")
                dict[c] += int(new[1])
    
    result = " - ".join(f"({k} : {v})" for k, v in dict.items())

    if all(value == 0 for value in dict.values()):
        return " "
        
    return result


b = ["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"]
c = ["A", "B", "C", "D"]
print(stock_list(b, c), "(A : 0) - (B : 1290) - (C : 515) - (D : 600)")


b = ["XXX 0", "RRRR 0", "DDDD 0", "BBB 0"]
c = ["X", "B", "R", "D"]
print(stock_list(b, c), " ")

