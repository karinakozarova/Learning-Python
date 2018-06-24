def remove_values_from_list(the_list, val):
   return [value for value in the_list if value != val]
  
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    s = set(arr)
    arr = list(s)
    arr.sort()
    print(arr[len(arr)- 2] )


  
    