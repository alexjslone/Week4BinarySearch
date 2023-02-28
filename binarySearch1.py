import math


#keys = [1, 5, 8, 12, 13]
#query = [8, 1, 23, 1, 11]



def binary_search(keys, query):
    #find initial midpoint
    indexMidKeys= math.floor(num_keys/2)

    finalList = []
    count = 0
    while count<num_queries:
    #have to include a condition for what to do if the number isn't in the list 
        if indexMidKeys == 0 and input_queries[count] != input_keys[indexMidKeys]:
            finalList.append(-1)
            count+=1
        elif indexMidKeys==num_keys-1  and input_queries[count] != input_keys[indexMidKeys]:
            finalList.append(-1)
            count+=1
        elif input_queries[count] == input_keys[indexMidKeys]:
            finalList.append(input_keys.index(input_keys[indexMidKeys]))
            count+=1
        elif input_queries[count] < input_keys[indexMidKeys]:
            indexMidKeys = math.floor((indexMidKeys/2))
        else: 
            indexMidKeys= math.floor((num_keys - indexMidKeys/2)+indexMidKeys)
    return finalList

if __name__ == '__main__':
    num_keys = int(input())
    input_keys = list(map(int, input().split()))
    assert len(input_keys) == num_keys

    num_queries = int(input())
    input_queries = list(map(int, input().split()))
    assert len(input_queries) == num_queries

    for q in input_queries:
        print(binary_search(input_keys, q), end=' ')
