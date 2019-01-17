class RomanNumeralizer:
    """
    Converts an integer input into its Roman Numeral equivalent
    """

    def __init__(self, dictionary):
        self.dictionary = dictionary

    def _correct_nines(self, string):
        string = list(string)
        for i in range(len(string)-2):
            if string[i] == string[i+2] != string[i+1]:
                string[i] = ""
                string[i+2] = list(self.dictionary.keys())[list(self.dictionary.values()).index(self.dictionary[string[i+2]]*2)]
        return ''.join(string)

    def _assign_roman_numerals(self):
        index, list_of_keys = 0, []
        for key, value in self.dictionary.items():
            list_of_keys += key
            if self._int//value > 0 and self._int//value < 4:
                for i in range(self._int//value):
                    self._characaters += key
                self._int = self._int % value
            elif self._int//value == 4:           # correct 4's
                self._characaters += key
                self._characaters += list_of_keys[index-1]
                self._int = self._int % value
            index += 1
        return self._characaters

    def convert_int_to_roman_numeral_characters(self, _int):
        self._int = _int
        self._characaters = ''
        return self._correct_nines(self._assign_roman_numerals())

if __name__ == "__main__":

    Dictionary = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    
    r = RomanNumeralizer(Dictionary)
    print(r.convert_int_to_roman_numeral_characters(2019))