import unittest

def Add(numbers):
    if numbers == "":
        return 0
    parts=str(numbers).split(',' or '\n')
    sum = 0
    for part in parts:
        sum += int(part)
    return sum

class TestStringCalculator(unittest.TestCase):
   

    def test_empty(self):
        self.assertEqual(Add(""),0)

    def test_one(self):
        self.assertEqual(Add("1"),1)

    def test_two(self):
        self.assertEqual(Add("1,2"),3)

    def test_multiple(self):
        self.assertEqual(Add("1,2,3,4"), 10)

    def test_invalid_format(self):
        with self.assertRaises(ValueError):(Add("Errorro"))

    def test_add_with_newlines(self):
        self.assertEqual(Add("1,\n2,3"),6)

if __name__ == '__main__':
    unittest.main()
