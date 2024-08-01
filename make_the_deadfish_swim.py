# Write a simple parser that will parse and run Deadfish.

# Deadfish has 4 commands, each 1 character long:

# i increments the value (initially 0)
# d decrements the value
# s squares the value
# o outputs the value into the return array
# Invalid characters should be ignored.

# parse("iiisdoso")  ==>  [8, 64]

def parse(data):
    array = []
    increment = 0
    for letter in data:
        if letter == "i":
            increment += 1
        elif letter == "o":
            array.append(increment)
        elif letter == "d":
            increment -= 1
        elif letter == "s":
            increment = increment ** 2
            
    return array 


print(parse('ioioio'),[1,2,3])
print(parse("idoiido"), [0,1])
print(parse("isoisoiso"), [1,4,25])
