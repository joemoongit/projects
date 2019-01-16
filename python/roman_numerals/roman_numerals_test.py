import unittest
from roman_numerals import RomanNumeralizer

class TestRomanNumeralizer(unittest.TestCase):
    """
    Tests for Roman Numeralizer (ignore the input, please enter any integer)
    """

    def test(self):
        Dictionary = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        self.r = RomanNumeralizer(Dictionary)
        assert self.r.return_roman_numeral(1999) == "MCMXCIX"
        assert self.r.return_roman_numeral(2000) != "MCMXCIX"
        assert self.r.return_roman_numeral(2019) == "MMXIX"


if __name__ == "__main__":
    unittest.main()