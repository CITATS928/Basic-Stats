from typing import List
from statzcw.zcount import zcount
from statzcw.zmean import zmean
from statzcw.zstddev import zstddev

def zcorr(datax: List[float], datay: List[float]) -> float :
    return cov(datax,datay)/(zstddev(datax)*zstddev(datay))


def cov(datax,datay):
    sum =0
    if zcount(datax)==zcount(datay):
        for i in range(0,zcount(datax)):
            sum+=((datax[i]-zmean(datax))*(datay[i]-zmean(datay)))
        return sum/(zcount(datax)-1)