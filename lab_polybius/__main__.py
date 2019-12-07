from lab_polybius.polybius import Polybius
from lab_polybius.constants import RU_LOWERCASE, RU_UPPERCASE, SYMBOLS

polybius = Polybius(RU_LOWERCASE + RU_UPPERCASE + SYMBOLS)
polybius.print_polybius_square()

phrase = input('Введите фразу (на русском), подлежащую шифрованию: ')

encoded_phrase = polybius.encode_phrase(phrase)
print('Кодированная фраза:', encoded_phrase)

decoded_phrase = polybius.decode_phrase(encoded_phrase)
print('Декодированная фраза:', decoded_phrase)
