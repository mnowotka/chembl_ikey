__author__ = 'mnowotka'

import unittest
from chembl_ikey.ikey import inchiToInchiKey

class TestIKey(unittest.TestCase):
    def test_morphineInChIKey(self):
        key = inchiToInchiKey("InChI=1S/C17H19NO3/c1-18-7-6-17-10-3-5-13(20)16(17)21-15-12(19)4-2-9(14(15)17)8-11(10)18/h2-5,10-11,13,16,19-20H,6-8H2,1H3/t10-,11+,13-,16-,17-/m0/s1")
        self.assertEqual(key,'BQJCRHHNABKAKU-KBQPJGBKSA-N')


if __name__ == '__main__':
    unittest.main()