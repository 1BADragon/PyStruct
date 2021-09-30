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

    def test_basicpack(self):
        s = BasicStruct()

        s.a = 9
        s.b = 3

        self.assertEqual(s._pack(), b'\x00\x00\x00\x09\x03')

if __name__ == "__main__":
    unittest.main()