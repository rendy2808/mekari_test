import unittest

from stage_zero import stage_zero

class StageZeroTest(unittest.TestCase):
    def test_stage_zero_one(self):
        self.assertEqual(stage_zero([3, 100, 145, 400]), 400)
    def test_stage_zero_two(self):
        self.assertEqual(stage_zero([ -1, 1000, -100000, 89, 433 ]), 1000)

if __name__ == '__main__':
    unittest.main()
