#!/usr/bin/env python3
import unittest

from pystruct import *

class BasicStruct(PyStruct):
    a = field(u32)
    b = field(i8)
class CStructTests(unittest.TestCase):
    def test_usable(self):
        s = BasicStruct()
        s.a = 34
        s.b = 1
        
        self.assertEqual(s.a, 34)
        self.assertEqual(s.b, 1)

    def test_notafield(self):
        s = BasicStruct()

        with self.assertRaises(AttributeError):
            s.c = 5

if __name__ == "__main__":
    unittest.main()