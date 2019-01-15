import unittest
from roman_numerals import RomanNumeralizer

class TestRomanNumeralizer(unittest.TestCase):
    """
    Tests for Roman Numeralizer (ignore the input, please enter any integer)
    """

    def test(self):
        Dictionary = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        self.r = RomanNumeralizer(Dictionary)
        assert self.r.correct_nines(self.r.return_roman_numerals(1999)) == "MCMXCIX"
        assert self.r.correct_nines(self.r.return_roman_numerals(2000)) != "MCMXCIX"


if __name__ == "__main__":
    unittest.main()