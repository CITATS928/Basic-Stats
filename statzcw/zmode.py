
from statzcw.zcount import zcount
from typing import List

def zmode(data: List[float]) -> float :
    counter,counter2 =1,0
    result=0
    sort_in_order(data)
    for i in range(0,zcount(data)-1):
        if data[i]==data[i+1]:
            counter+=1
        else:
            counter=1
        if counter>counter2:
            counter2=counter
            result=data[i]
    return result


def sort_in_order(arr: List):
    n = zcount(arr)
    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j+1] < arr[j]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr



#test
#datat=[2,6,3,5,7,6,7,8,8,8,3]
#print(sort_in_order(datat))
#print(zmode(datat))


##why is working
##print(max(set(datat), key = datat.count))
