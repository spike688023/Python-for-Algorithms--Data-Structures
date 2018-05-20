def pair_sum(arr,k):
    
    #arr.sort()
    #print(arr)
    #count = 0
    dict1 = {}
    list1 = []
    for i in arr:
        dict1[i] = dict1.get(i,0) + 1
    
    for i in arr:
        target = k - i
        if dict1.get(target, 0) > 0 and dict1.get(i, 0) > 0:
            #count += 1
            dict1[target] -= 1
            dict1[i] -= 1
            list1.append((i,target))
    
    return len(list(set(list1)))