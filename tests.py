import unittest 
import statistics

# Median Calculation
def median_calculation(prices):
    median = statistics.median(prices)
    return median 

# Test Cases for Median Check
class TestMyFunction(unittest.TestCase): 
    def __init__(self, methodName='runTest', param1=None, param2=None): 
        super(TestMyFunction, self).__init__(methodName) 
        self.param1 = param1 
        self.param2 = param2
         
    def test_median(self): 
        result = median_calculation(self.param1) 
        self.assertEqual(result, self.param2) 

def suite(prices_list,median): 
    test_suite = unittest.TestSuite() 
    test_suite.addTest(TestMyFunction('test_median', param1=prices_list, param2=median)) 
    return test_suite 
# if __name__ == '__main__': 
    