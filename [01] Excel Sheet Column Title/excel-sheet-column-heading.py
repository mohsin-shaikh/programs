columnNumber = 26 

# define an alphabet
alfa = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# Z  => 26
# AA => 27
# AB => 28
# ...
# AZ => 52
# ...

def convertToTitle(index): 
    s = ""
    if (index == 1): 
        return "A"
    while (index > 0): 
        r = round(index % 26)
        if (r == 0):
            s += "Z"
            index = index - 26
        else:
            s += alfa[r - 1]
            index = round(index / 26)   
    return s[::-1]

print(convertToTitle(28))

# 27
# if false
# while true
# reminder 1
# else
# s = A
# 1