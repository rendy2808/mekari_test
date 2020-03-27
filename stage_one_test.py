import unittest

from stage_one import short_letter

class StageOneTest(unittest.TestCase):
    def test_stage_one_one(self):
        self.assertEqual(short_letter("Negara Kesatuan Republik Indonesia"), "NKRI")
    def test_stage_one_two(self):
        self.assertEqual(short_letter("Kereta Api Indonesia"), "KAI")

if __name__ == '__main__':
    unittest.main()
