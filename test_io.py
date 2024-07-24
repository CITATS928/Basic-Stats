from datareader import readDataSets, readDataFile
from sys import argv
import unittest

class TestIO(unittest.TestCase):
    def test_readDataFile(self):
        x,y = readDataFile('dataOne.csv')
        self.assertEqual(len(x),len(y))
        self.assertIsInstance(x[0],float)
        self.assertIsInstance(y[0],float)

    def test_readDataSet(self):
        datasets = ['dataOne.csv', 'dataTwo.csv', 'dataThree.csv', 'dataZero.csv']
        data=readDataSets(datasets)
        self.assertEqual(len(data),4)




if __name__ == "__main__":
    unittest.main()