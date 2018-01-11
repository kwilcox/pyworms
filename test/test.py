import unittest
import sys
import os
import logging
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../")))
import pyworms

class Test(unittest.TestCase):

    def setUp(self):
        logging.disable(logging.CRITICAL)

    def testAphiaRecordByAphiaID(self):

        res = pyworms.aphiaRecordByAphiaID(9999999)
        self.assertIsNone(res)

        res = pyworms.aphiaRecordByAphiaID(123456)
        self.assertIsNotNone(res)

        with self.assertRaises(Exception):
            res = pyworms.aphiaRecordByAphiaID("abcd")

    def testCache(self):
        pyworms.aphiaRecordByAphiaID.cache_clear()
        self.assertEquals(pyworms.aphiaRecordByAphiaID.cache_info()[3], 0)
        res = pyworms.aphiaRecordByAphiaID(123459)
        self.assertEquals(pyworms.aphiaRecordByAphiaID.cache_info()[3], 1)