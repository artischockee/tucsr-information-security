import math
import random
import numpy as np

from lab_matrix_multi.utils import get_appropriate_phrase_len, divide_chunks


class MatrixMulti:
    def __init__(self, dictionary: list, augment_symbol: str):
        self.__dictionary = dictionary
        self.__augment_symbol = augment_symbol
        self.__key_matrix_side = 3

    def get_dictionary_length(self) -> int:
        return len(self.__dictionary)

    def __get_processed_phrase(self, phrase: str) -> str:
        phrase_len = len(phrase)

        if phrase_len < self.__key_matrix_side:
            pass  # TODO

        appropriate_phrase_len = get_appropriate_phrase_len(self.__key_matrix_side, phrase_len)
        processed_phrase = phrase
        if appropriate_phrase_len > phrase_len:
            augment_symbols_amount = appropriate_phrase_len - phrase_len
            while augment_symbols_amount > 0:
                processed_phrase += self.__augment_symbol
                augment_symbols_amount -= 1

        return processed_phrase

    def __get_key_matrix(self):
        random_lower_bound = 1
        random_upper_bound = 5

        matrix_rows = []
        for i in range(self.__key_matrix_side):
            matrix_cols = []
            for j in range(self.__key_matrix_side):
                matrix_cols.append(random.randint(random_lower_bound, random_upper_bound))
            matrix_rows.append(matrix_cols)

        return matrix_rows

    def get_index_of_letter(self, letter: str) -> int:
        index = -1
        try:
            index = self.__dictionary.index(letter)
            return index + 1
        except ValueError:
            return index

    def get_letter_by_index(self, index: int) -> str:
        if index not in range(self.get_dictionary_length()):
            return ''
        return self.__dictionary[index]

    def __get_pre_encrypted_phrase(self, phrase: str) -> list:
        pre_encrypted_phrase = []
        for letter in phrase:
            encrypted_letter = self.get_index_of_letter(letter)
            pre_encrypted_phrase.append(encrypted_letter)

        return pre_encrypted_phrase

    @staticmethod
    def get_multiplication_result(chunk: list, matrix: list) -> list:
        total_result = []
        for cols in matrix:
            cell_result = 0
            for i in range(len(cols)):
                cell_result += cols[i] * chunk[i]
            total_result.append(cell_result)

        return total_result

    def encrypt(self, phrase: str) -> list:
        processed_phrase = self.__get_processed_phrase(phrase)

        pre_encrypted_phrase = self.__get_pre_encrypted_phrase(processed_phrase)
        key_matrix = self.__get_key_matrix()

        chunks = list(divide_chunks(pre_encrypted_phrase, self.__key_matrix_side))

        print('key_matrix', key_matrix)

        encrypted_phrase = []

        for chunk in chunks:
            encrypted_phrase += self.get_multiplication_result(chunk, key_matrix)

        return encrypted_phrase

    def decrypt(self, phrase: list, key_sequence: list) -> str or None:
        if len(key_sequence) != math.pow(self.__key_matrix_side, 2):
            print('Key matrix size is not appropriate for the decryption process. Abort.')
            return

        phrase_chunks = list(divide_chunks(phrase, self.__key_matrix_side))
        key_matrix = np.array(list(divide_chunks(key_sequence, self.__key_matrix_side)))
        key_matrix_inverted = np.linalg.inv(key_matrix)

        pre_decrypted_phrase = []
        for chunk in phrase_chunks:
            chunk_multiplication_result = key_matrix_inverted.dot(np.array(chunk))
            pre_decrypted_phrase += list(chunk_multiplication_result)

        decrypted_phrase = ''
        for number in pre_decrypted_phrase:
            decrypted_phrase += self.get_letter_by_index(int(round(number)) - 1)

        return decrypted_phrase
