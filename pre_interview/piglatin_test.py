import unittest
from piglatin import PigLatin

class TestpigLatin(unittest.TestCase):

    def test_find_subsequent_ques_isTrue(self):
        self.assertTrue(PigLatin().find_subsequent_ques("arrb6???4xxbl5???eee5"))
    
    def test_find_subsequent_ques_isFalse(self):
        self.assertFalse(PigLatin().find_subsequent_ques("5??aaaaaaaaaaaaaaaaaaa?5?5"))


if __name__ == '__main__':
    unittest.main()