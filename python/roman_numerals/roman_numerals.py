class RomanNumeralizer:
    """
    Converts an integer input into its Roman Numeral equivalent
    """

    def __init__(self, dictionary):
        self.number = int(input("Enter integer to convert to roman numerals: "))
        self.letter = ''
        self.dictionary = dictionary

    # for readability
    def correct_nines(self, string):
        string = list(string)
        for i in range(len(string)-2):
            if string[i] == string[i+2] != string[i+1]:
                string[i] = ""
                string[i+2] = list(self.dictionary.keys())[list(self.dictionary.values()).index(self.dictionary[string[i+2]]*2)]
        return ''.join(string)

    def return_roman_numerals(self, number = None):
        if number:
            self.number = number

        index, list_of_keys = 0, []
        for key, value in self.dictionary.items():
            list_of_keys += key
            if self.number//value > 0 and self.number//value < 4:
                for i in range(self.number//value):
                    self.letter += key
                self.number = self.number % value
            elif self.number//value == 4:           # correct 4's
                self.letter += key
                self.letter += list_of_keys[index-1]
                self.number = self.number % value
            index += 1
        return self.letter

if __name__ == "__main__":

    Dictionary = {"M":1000, "D":500, "C":100, "L":50, "X":10, "V":5, "I":1}
    
    r = RomanNumeralizer(Dictionary)
    print(r.correct_nines(r.return_roman_numerals()))