from lab_rsa.utils import get_coprime_integer, lcm


class Rsa:
    def __init__(self, dictionary: list):
        self.__dictionary = dictionary

    def get_dictionary_length(self) -> int:
        return len(self.__dictionary)

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

    def foo_get_d(self, e, phin):
        safe_iteration_amount = 10_000
        iterator = 1
        while safe_iteration_amount > 0:
            safe_iteration_amount -= 1
            if (iterator * e) % phin == 1 and iterator != e:
                return iterator
            iterator += 1
        return 0

    def get_encryption_keys(self) -> list:
        p = 61  # TODO add random prime number
        q = 53  # TODO add random prime number
        n = p * q
        phin = int(lcm(p - 1, q - 1))
        e = get_coprime_integer(phin)

        d = self.foo_get_d(e, phin)

        public_key = [e, n]
        private_key = [d, n]

        return [public_key, private_key]

    def encrypt(self, phrase: str) -> list:
        [public_key, private_key] = self.get_encryption_keys()

        encrypted_phrase = []
        for letter in phrase:
            letter_index = self.get_index_of_letter(letter)
            encrypted_letter = round(pow(letter_index, public_key[0]) % public_key[1])
            encrypted_phrase.append(encrypted_letter)

        return [encrypted_phrase, public_key, private_key]

    def decrypt(self, phrase: list, private_key: list) -> str:
        decrypted_phrase = ''
        for encrypted_letter in phrase:
            letter_index = round(pow(encrypted_letter, private_key[0]) % private_key[1])
            decrypted_letter = self.get_letter_by_index(letter_index - 1)
            decrypted_phrase += decrypted_letter

        return decrypted_phrase
