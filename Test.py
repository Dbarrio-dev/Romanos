import unittest

from Romanos import *

class RomanosTest(unittest.TestCase):
    
    def test_single_simbol(self):
        self.assertEqual(romano_a_entero("M"),1000)
        self.assertEqual(romano_a_entero("D"),500)
        self.assertEqual(romano_a_entero("C"),100)
        self.assertEqual(romano_a_entero("L"),50)
        self.assertEqual(romano_a_entero("X"),10)
        self.assertEqual(romano_a_entero("V"),5)
        self.assertEqual(romano_a_entero("I"),1)

        self.assertRaises(ValueError, romano_a_entero, 'z')
        self.assertRaises(ValueError, romano_a_entero, '23')

    def test_MMM(self):
        self.assertEqual(romano_a_entero("MMM"),3000)

    def test_MMMM(self):
        self.assertRaises(OverflowError, romano_a_entero, 'MMMM')

#CC 200  
#III 3
#XX20
#W Overflowerror('Demasiados simbolos de tipo V') 

if __name__ == '__main__':
    unittest.main()

