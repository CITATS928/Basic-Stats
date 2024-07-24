from typing import List
from statzcw.zcount import zcount

def zmean(data: List[float]) -> float :
    return sum(data)/zcount(data)

#print(zmean(([10,10,10,10,])))