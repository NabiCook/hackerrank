if __name__ == '__main__':
    N = int(input())
    list = []
    inputlist = []

    for i in range(N):
        data = input()
        if data == "print":
            print(list)
        if data == "sort":
            list.sort()
        if data == "reverse":
            list.reverse()
        if data == "pop":
            list.pop()
        else:
            inputlist = data.split(" ")
            if inputlist[0] == "insert":
                list.insert(int(inputlist[1]), int(inputlist[2]))              

            if inputlist[0] == "append":
                list.append(int(inputlist[1]))  
                
            if inputlist[0] == "remove":
                list.remove(int(inputlist[1]))  


                
