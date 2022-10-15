import unittest
from main import isArray, isEnum, isInteger, isString, checkType

class TestData(unittest.TestCase):
    
    def test_isEnum(self):
        self.assertEqual(isEnum(["","",""]), True)
        self.assertNotEqual(isEnum(["test", {}]), True)
        self.assertEqual(isEnum([[], ""]), False)
        self.assertNotEqual(isEnum("test"), True)
        self.assertEqual(isEnum(1234), False)

    def test_isArray(self):
        self.assertEqual(isArray({}), False)
        self.assertEqual(isArray([{}]), True)
        self.assertNotEqual(isArray([{}, '']), True)
        self.assertNotEqual(isArray([{}, 1234]), True)


    def test_isString(self):
        self.assertEqual(isString(""), True)
        self.assertEqual(isString("[]"), True)
        self.assertEqual(isString("1234"), True)
        self.assertNotEqual(isString(1234), True)
        self.assertNotEqual(isString("{}"), False)

    def test_isInteger(self):
        self.assertEqual(isInteger(4), True)
        self.assertEqual(isInteger(""), False)
        self.assertNotEqual(isInteger("4"), True)
        self.assertNotEqual(isInteger([1, 2, 3, 4]), True)
        self.assertNotEqual(isInteger({"one": 123}), True)

    def test_checkType(self):
        self.assertEqual(checkType(4), "INTEGER")
        self.assertEqual(checkType(""), "STRING")
        self.assertEqual(checkType(["", ""]), "ENUM")
        self.assertEqual(checkType([{}]), "ARRAY")
        self.assertEqual(checkType(False), "NOT A REQUESTED TYPE")
        self.assertEqual(checkType({}), "NOT A REQUESTED TYPE")
        self.assertEqual(checkType(["", {}]), "NOT A REQUESTED TYPE")

