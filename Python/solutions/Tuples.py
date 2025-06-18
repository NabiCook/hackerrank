if __name__ == '__main__':
    n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))

#this was a weird question. hash function apparently
#generates different value dependingo on python2 or python3
#and the answers were based on python2.
#plus, the first integer had no purpose as an input.
#just printing the hash values were good enough to solve the problem