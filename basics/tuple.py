if __name__ == '__main__':
    n = int(input())
    vars = input().split()
    integer_list = map(int, vars)    
    print(hash(tuple(integer_list)))