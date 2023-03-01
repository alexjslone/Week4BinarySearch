import math


input_keys = [1,4,6,11,13]
input_queries = [1,2,3,11,12]
num_keys= len(input_keys)
num_queries = len(input_queries)


def binary_search(input_keys, input_queries):
    #find initial midpoint
    indexMidKeys= math.floor(num_keys/2)

    #finalList = []
    count = 0
    while count< num_keys:
    #have to include a condition for what to do if the number isn't in the list 
        #print(count)
        if indexMidKeys == 0 and input_queries[count] != input_keys[indexMidKeys]:
            input_queries[count]=-1
            count+=1
            indexMidKeys=math.floor(num_keys/2)
        elif indexMidKeys==num_keys-1  and input_queries[count] != input_keys[indexMidKeys]:
            input_queries[count]=-1
            count+=1
            indexMidKeys=math.floor(num_keys/2)
        elif input_queries[count] == input_keys[indexMidKeys]:
            input_queries[count]=(input_keys.index(input_keys[indexMidKeys]))
            count+=1
            indexMidKeys=math.floor(num_keys/2)
        elif input_keys[indexMidKeys-1]<input_queries[count]<input_keys[indexMidKeys]:
            input_queries[count]=-1
            count+=1
            indexMidKeys=math.floor(num_keys/2)
        elif input_queries[count] < input_keys[indexMidKeys]:
            indexMidKeys = math.floor((indexMidKeys/2))
        elif input_queries[count] > input_keys[indexMidKeys]: 
            indexMidKeys= math.floor((num_keys - indexMidKeys)/2+indexMidKeys)
    for i in input_queries: 
        print(i)
binary_search(input_keys, input_queries)


""""
if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    binary_search(input_keys, input_queries)
"""