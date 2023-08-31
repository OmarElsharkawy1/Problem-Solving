import unittest
import valid_parentheses

class TestValidParentheses(unittest.TestCase):
    def test(self):
        self.assertEqual(valid_parentheses.isValid('()'), True)
        self.assertEqual(valid_parentheses.isValid('({})'), True)
        self.assertEqual(valid_parentheses.isValid('({(})'), False)
        self.assertEqual(valid_parentheses.isValid('))()[]'), False)

if __name__ == '__main__':
    unittest.main()