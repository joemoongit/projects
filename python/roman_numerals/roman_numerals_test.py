import unittest
from roman_numerals import RomanNumeralizer

class TestRomanNumeralizer(unittest.TestCase):
    """
    Tests for Roman Numeralizer
    """

    def test(self):
        Dictionary = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
        self.r = RomanNumeralizer(Dictionary)
        assert self.r.convert_int_to_roman_numeral_characters(1999) == "MCMXCIX"
        assert self.r.convert_int_to_roman_numeral_characters(2000) != "MCMXCIX"
        assert self.r.convert_int_to_roman_numeral_characters(2019) == "MMXIX"
        assert self.r.convert_int_to_roman_numeral_characters(1976) == "MCMLXXVI"


if __name__ == "__main__":
    unittest.main()