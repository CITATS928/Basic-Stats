from typing import List
from statzcw.zmean import zmean

def zvariance(data: List[float]) -> float :
    deviations=[]
    for x in data:
        deviations.append((x-zmean(data))**2)

    return sum(deviations)/(len(data)-1)

#datat=[2,6,3,5,7,6,7,8,8,8,3]
#print(zvariance(datat))