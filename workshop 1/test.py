import unittest
import source 


class TestCalc(unittest.TestCase):
    def testSub1(self): 
        self.assertEqual(4, source.performSub(5, 1), "Bug in code!" )

    def testSub2(self):
        self.assertEqual(1, source.performSub(2, 1), "Bug in code!")

class TestAddition(unittest.TestCase):
    def testAddition1(self): 
        self.assertEqual(3, source.performAdd(2, 1), "Error in implementation.")

    def testAddition2(self): 
        self.assertEqual(0, source.performAdd(1, -1), "Error in code!")
        
class TestMult(unittest.TestCase):
    def testMult1(self):
        self.assertEqual(25, source.performMult(5, 5), "Bug in code!")
        
    def testMult2(self):
        self.assertEqual(0, source.performMult(3, 0), "Bug in code!")
        
    def testMult3(self):
        self.assertEqual(-2, source.performMult(2, -1), "Bug in code!")
        
class TestDiv(unittest.TestCase):
    def testDiv1(self):
        self.assertEqual(5, source.performDiv(5, 1), "Bug in code!")
        
    def testDiv2(self):
        self.assertEqual(0, source.performDiv(0, 1), "Bug in code!")
        
    def testDiv3(self):
        self.assertEqual("Cannot divide by 0.", source.performMult(3, 0), "Bug in code!")
        
    def testDiv2(self):
        self.assertEqual(-1, source.performDiv(-5, 5), "Bug in code!")
        

if __name__ == '__main__': 
    unittest.main() 
