import pandas as pd


class DigitAnalyzer:
    DICT_DIGITS = {0: '',
                   1: '',
                   2: '',
                   3: '',
                   4: '',
                   5: '',
                   6: '',
                   7: '',
                   8: '',
                   9: ''}

    def __init__(self, series: pd.Series):
        for val in series:
            self.__find_obvious_digit_of_segment(val)
        for val in series[::-1]:
            self.__find_digit_of_segment(val)

    def __set_zero(self, segment: str):
        if len(segment) == 6 and self.DICT_DIGITS[1] and self.DICT_DIGITS[4]:
            zero = set(segment)
            one = set(self.DICT_DIGITS[1])
            four = set(self.DICT_DIGITS[4])
            if len(one.difference(zero)) == 0 and len(four.difference(zero)) == 1:
                self.DICT_DIGITS[0] = segment

    def __set_one(self, segment: str):
        if len(segment) == 2:
            self.DICT_DIGITS[1] = segment

    def __set_two(self, segment: str):
        if len(segment) == 5 and self.DICT_DIGITS[4] and self.DICT_DIGITS[7]:
            two = set(segment)
            four = set(self.DICT_DIGITS[4])
            seven = set(self.DICT_DIGITS[7])
            if len(four.difference(two)) == 2 and len(seven.difference(two)) == 1:
                self.DICT_DIGITS[2] = segment

    def __set_three(self, segment: str):
        if len(segment) == 5 and self.DICT_DIGITS[4] and self.DICT_DIGITS[7]:
            three = set(segment)
            four = set(self.DICT_DIGITS[4])
            seven = set(self.DICT_DIGITS[7])
            if len(four.difference(three)) == 1 and len(seven.difference(three)) == 0:
                self.DICT_DIGITS[3] = segment

    def __set_four(self, segment: str):
        if len(segment) == 4:
            self.DICT_DIGITS[4] = segment

    def __set_five(self, segment: str):
        if len(segment) == 5 and self.DICT_DIGITS[4] and self.DICT_DIGITS[7]:
            five = set(segment)
            four = set(self.DICT_DIGITS[4])
            seven = set(self.DICT_DIGITS[7])
            if len(four.difference(five)) == 1 and len(seven.difference(five)) == 1:
                self.DICT_DIGITS[5] = segment

    def __set_six(self, segment: str):
        if len(segment) == 6 and self.DICT_DIGITS[1] and self.DICT_DIGITS[4]:
            six = set(segment)
            one = set(self.DICT_DIGITS[1])
            four = set(self.DICT_DIGITS[4])
            if len(one.difference(six)) == 1 and len(four.difference(six)) == 1:
                self.DICT_DIGITS[6] = segment

    def __set_seven(self, segment: str):
        if len(segment) == 3:
            self.DICT_DIGITS[7] = segment

    def __set_eight(self, segment: str):
        if len(segment) == 7:
            self.DICT_DIGITS[8] = segment

    def __set_nine(self, segment: str):
        if len(segment) == 6 and self.DICT_DIGITS[1] and self.DICT_DIGITS[4]:
            nine = set(segment)
            one = set(self.DICT_DIGITS[1])
            four = set(self.DICT_DIGITS[4])
            if len(one.difference(nine)) == 0 and len(four.difference(nine)) == 0:
                self.DICT_DIGITS[9] = segment

    def __find_obvious_digit_of_segment(self, segment: str):
        self.__set_one(segment)
        self.__set_four(segment)
        self.__set_seven(segment)
        self.__set_eight(segment)

    def __find_digit_of_segment(self, segment: str):
        self.__set_zero(segment)
        self.__set_two(segment)
        self.__set_three(segment)
        self.__set_five(segment)
        self.__set_six(segment)
        self.__set_nine(segment)

    def convert_segment_to_digit(self, segment: str) -> int:
        segment = set(segment)
        for key, value in self.DICT_DIGITS.items():
            if set(value) == segment:
                return key


df = pd.read_csv('input.txt', header=None, dtype=str, delimiter=' ')

df_input = df.iloc[:, :10]
df_output = df.iloc[:, 11:]

SUM_OUTPUTS = 0

for ind in range(len(df_input)):
    analyzer = DigitAnalyzer(df_input.iloc[ind])
    digits = ''.join([str(analyzer.convert_segment_to_digit(val)) for val in df_output.iloc[ind]])
    SUM_OUTPUTS += int(digits)

print(SUM_OUTPUTS)
