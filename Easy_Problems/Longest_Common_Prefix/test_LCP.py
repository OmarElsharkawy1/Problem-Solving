import unittest
import longest_common_prefix

class TestLongestCommonPrefix(unittest.TestCase):

    def test(self):
        self.assertEqual(longest_common_prefix.longestCommonPrefix(['cat', 'car', 'carpenter']), 'ca')
        self.assertEqual(longest_common_prefix.longestCommonPrefix(['cartoon', 'cartoons', 'carpenter']), 'car')
        self.assertEqual(longest_common_prefix.longestCommonPrefix(['dog', 'animal']), '')
    

if __name__ == '__main__':
    unittest.main()