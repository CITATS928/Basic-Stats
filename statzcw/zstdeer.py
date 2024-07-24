from typing import List
from statzcw.zstddev import zstddev
from statzcw.zcount import zcount


def zstderr(data: List[float]) -> float :
    return zstddev(data)/((zcount(data))**0.5)

    