input = "HackerRank.com presents 'Pythonist 2'."
#expected output = hACKERrANK.COM PRESENTS "pYTHONIST 2".

#swapcase basically does everything :o
#was initially thinking capitalize loop and then lower case loop
def swap_case(s):
    change = s.swapcase()
    return(change)

print(swap_case(input))