
def split_and_join(line):  
    #looks for " " then replaces it with "-"
    change = line.replace(" ", "-")
    return(change)

#expected output is "this-is-a-string"
input = "this is a string"
split_and_join(input)


