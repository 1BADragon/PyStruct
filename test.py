#!/usr/bin/env python3
import unittest
import struct

from pystruct import *

class BasicStruct(PyStruct):
    a = field(u32)
    b = field(i8)

class ArrayStruct(PyStruct):
    a = field(u32)
    arr = field(Array(u32, 4, default=0))

class NestedStruct(PyStruct):
    a = field(u32)
    b = field(BasicStruct)

class NestedArraySruct(PyStruct):
    a = field(u32)
    b = field(Array(BasicStruct, 2))

class PropertyStruct(PyStruct):
    a = field(u32)

    @property
    def even(self):
        return self.a % 2 == 0

class StringStruct(PyStruct):
    a = field(u32)
    s = field(String(16))
    
class PyStructTests(unittest.TestCase):
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

    def test_basicunpack(self):
        s = BasicStruct()

        s._unpack(b'\x00\x00\x00\x09\x03')

        self.assertEqual(s.a, 9)
        self.assertEqual(s.b, 3)

    def test_compat(self):
        s = BasicStruct()
        s2 = BasicStruct()

        s.a = 9
        s.b = 34

        s2._unpack(s._pack())

        self.assertEqual(s.a, 9)
        self.assertEqual(s.b, 34)
        
    def test_empty(self):
        s = BasicStruct()

        self.assertEqual(s._pack(), struct.pack("!IB", 0, 0))

    def test_packarray(self):
        s = ArrayStruct()

        s.a = 34
        s.arr[3] = 45

        self.assertEqual(s._pack(), struct.pack("!IIIII", 34, 0, 0, 0, 45))

    def test_unpackarray(self):
        s = ArrayStruct()

        s._unpack(struct.pack("!IIIII", 34, 0, 0, 0, 45))

        self.assertEqual(s.a, 34)
        self.assertEqual(s.arr[3], 45)

    def test_properties(self):
        s = PropertyStruct()

        s.a = 56

        self.assertEqual(s.even, True)

    def test_nested(self):
        s = NestedStruct()

        s.a = 32
        s.b.a = 45
        s.b.b = 23

        self.assertEqual(s._pack(), struct.pack("!IIB", 32, 45, 23))

    def test_nested_array(self):
        s = NestedArraySruct()

        s.a = 32
        s.b[0].a = 45
        s.b[0].b = 23
        s.b[1].a = 33
        s.b[1].b = 78

        self.assertEqual(s._pack(), struct.pack("!IIBIB", 32, 45, 23, 33, 78))

    def test_string_pack(self):
        s = StringStruct()

        s.a = 32
        s.s = "a" * 16

        self.assertEqual(s._pack(), struct.pack("!I", 32) + b"a" * 16)

    def test_string_unpack(self):
        s = StringStruct()

        s._unpack(struct.pack("!I", 32) + b'a' * 16)

        self.assertEqual(s.a, 32)
        self.assertEqual(s.s, b'a' * 16)


if __name__ == "__main__":
    unittest.main()