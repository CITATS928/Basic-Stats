from typing import List
from statzcw.zvariance import zvariance

def zstddev(data: List[float]) -> float :
    # sqrt of variance
    return (zvariance(data))**0.5

#datat=[2,6,3,5,7,6,7,8,8,8,3]
#print(zstddev(datat))