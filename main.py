from statzcw.zcount import zcount
from statzcw.zmean import zmean
from statzcw.zmode import zmode
from statzcw.zmedian import zmedian
from statzcw.zvariance import zvariance
from statzcw.zstddev import zstddev
from statzcw.zstdeer import zstderr
from statzcw.zcorr import zcorr
from datareader import readDataSets


datasets = ['dataOne.csv', 'dataTwo.csv', 'dataThree.csv', 'dataZero.csv']

data = readDataSets(datasets)

for dataset in datasets:
    X, Y = data[dataset]

    print(f"Dataset: {dataset}")
    print(f"Count of X: {zcount(X)}")
    print(f"Count of Y: {zcount(Y)}")
    print(f"Mean of X: {zmean(X)}")
    print(f"Mean of Y: {zmean(Y)}")
    print(f"Sample Variance of X: {zvariance(X)}")
    print(f"Sample Variance of Y: {zvariance(Y)}")
    print(f"Correlation between X and Y: {zcorr(X, Y)}")
    print(f"Median of X: {zmedian(X)}")
    print(f"Median of Y: {zmedian(Y)}")
    print(f"Mode of X: {zmode(X)}")
    print(f"Mode of Y: {zmode(Y)}")
    print(f"Sample Std deviation of X: {zstddev(X)}")
    print(f"Sample Std deviation of Y: {zstddev(Y)}")
    print(f"Standard Error of the Mean of X: {zstderr(X)}")
    print(f"Standard Error of the Mean of Y: {zstderr(Y)}")
    print("\n")