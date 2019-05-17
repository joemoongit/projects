#
# Converts an Integer into a String (in roman numerals)
#
# (c) Joseph Moon, 2018
#

class RomanNumeralizer:
    """
    Converts an integer input into its Roman Numeral equivalent
    """

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def convert_int_to_roman_numeral_characters(self, _int):
        self._characaters = ''
        return self._correct_nines(self._assign_roman_numerals(_int))

    def _correct_nines(self, _string):
        _string = list(_string)
        for i in range(len(_string)-2):
            if _string[i] == _string[i+2] != _string[i+1]:
                _string[i] = ''
                _string[i+2] = list(self.dictionary.keys())[list(self.dictionary.values()).index(self.dictionary[_string[i+2]]*2)]
        return ''.join(_string)

    def _assign_roman_numerals(self, _int):
        index, list_of_keys = 0, []
        for key, value in self.dictionary.items():
            list_of_keys += key
            if _int//value > 0 and _int//value < 4:
                for i in range(_int//value):
                    self._characaters += key
                _int = _int % value
            elif _int//value == 4:           # correct 4's
                self._characaters += key
                self._characaters += list_of_keys[index-1]
                _int = _int % value
            index += 1
        return self._characaters

if __name__ == "__main__":
    Dictionary = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    r = RomanNumeralizer(Dictionary)
    print(r.convert_int_to_roman_numeral_characters(2019))
    print(r.convert_int_to_roman_numeral_characters(1999))
    print(r.convert_int_to_roman_numeral_characters(1876))