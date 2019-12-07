import math


class Polybius:
    def __init__(self, symbols):
        self.__polybius_square = Polybius.create_polybius_square(symbols)

    # creates Polybius square with optimized dimensions
    @staticmethod
    def create_polybius_square(symbols):
        symbols_len = len(symbols)
        rows_amount = math.floor(math.sqrt(symbols_len))
        cols_amount = math.ceil(symbols_len / rows_amount)

        polybius_square = []

        current_col = []
        for i in range(symbols_len):
            current_col.append(symbols[i])
            if len(current_col) == cols_amount:
                polybius_square.append(current_col)
                current_col = []

        return polybius_square

    def print_polybius_square(self):
        for i in range(len(self.__polybius_square)):
            print(self.__polybius_square[i])

    def get_index_of_letter(self, letter: str) -> str:
        index = ''
        for i in range(len(self.__polybius_square)):
            try:
                col_index = self.__polybius_square[i].index(letter)
            except ValueError:
                continue
            index = '{}{}'.format(i + 1, col_index + 1)
            break
        return index

    def get_letter_by_index(self, index: str) -> str:
        int_indexes = list(map(lambda x: int(x), index))
        return self.__polybius_square[int_indexes[0] - 1][int_indexes[1] - 1]

    def encode_phrase(self, phrase: str) -> str:
        encoded_phrase = ''

        phrase_len = len(phrase)
        for i in range(phrase_len):
            letter_index = self.get_index_of_letter(phrase[i])
            encoded_phrase += letter_index
            if i < phrase_len - 1:
                encoded_phrase += ' '

        return encoded_phrase

    def decode_phrase(self, phrase: str) -> str:
        decoded_phrase = ''

        phrase_indexes = phrase.split(' ')
        for i in range(len(phrase_indexes)):
            decoded_phrase += self.get_letter_by_index(phrase_indexes[i])

        return decoded_phrase
