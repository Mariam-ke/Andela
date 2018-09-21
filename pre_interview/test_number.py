import unittest
import number


class testTripleCheck(unittest.TestCase):
    def test_for_type(self):
        with self.assertRaises(TypeError):
            number.num_check(['1','2','3'])

    def test_for_correct_output(self):
        self.assertEqual(number.num_check([7,7,7,5,5,1,5]), (1, ))
        self.assertEqual(number.num_check([9,9,9,3,6,6,6]), (3, ))
        self.assertEqual(number.num_check([2,2,2,8,6,6,6]), (8, ))



if __name__ == '__main__':
    unittest.main()