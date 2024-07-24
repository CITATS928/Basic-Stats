from typing import List
from statzcw.zmode import sort_in_order
from statzcw.zcount import zcount

def zmedian(data: List[float]) -> float :
    sort_in_order(data)
    if zcount(data)%2!=0:
        return data[zcount(data)//2]
    else:

        return (data[zcount(data)//2]+data[zcount(data)//2-1])/2



#testdata=[0,1,2,3,4,5,9]
#print(zmedian(testdata))