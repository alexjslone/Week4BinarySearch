import math
#This one failed case #32/36 for taking too long 



#input_keys = [1,5, 8, 12,13]
#input_queries = [8, 1, 23, 1, 11]
#num_keys= len(input_keys)
#num_queries = len(input_queries)


def binary_search(input_keys, input_queries):
    newList = []
    for i in input_queries: 
        try: 
            input_keys.index(i)
        except ValueError: 
            newList.append(-1)
        else: 
            newList.append(input_keys.index(i))
    
    for i in newList: 
        print(i)

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    binary_search(input_keys, input_queries)
