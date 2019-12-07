import random
from lab_substitution.utils import get_greatest_number_of_range


class Substitution:
    def __init__(self, dictionary: list):
        self.__dictionary = dictionary
        self.__coefficient = random.randint(1, get_greatest_number_of_range(1, len(dictionary)))

    def get_dictionary_length(self) -> int:
        return len(self.__dictionary)

    def get_index_of_letter(self, letter: str) -> int:
        index = -1
        try:
            index = self.__dictionary.index(letter)
        except ValueError:
            pass
        finally:
            return index

    def get_letter_by_index(self, index: int) -> str:
        if index not in range(self.get_dictionary_length()):
            return ''
        return self.__dictionary[index]

    def encrypt(self, phrase: str, key: str) -> str:
        dict_len = self.get_dictionary_length()
        key_len = len(key)

        encrypted_phrase = ''

        key_index = 0
        for letter in phrase:
            phrase_letter_index = self.get_index_of_letter(letter) + 1

            if key_index == key_len:
                key_index = 0

            key_letter_index = self.get_index_of_letter(key[key_index]) + 1
            key_index += 1

            encrypted_letter = self.get_letter_by_index(
                (self.__coefficient * phrase_letter_index + key_letter_index) % dict_len - 1)
            encrypted_phrase += encrypted_letter

        return encrypted_phrase

    def decrypt(self, phrase: str, key: str) -> str:
        for letter in phrase:
            pass