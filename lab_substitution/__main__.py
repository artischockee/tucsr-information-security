from lab_substitution.substitution import Substitution
from lab_substitution.constants import RU_LOWERCASE, RU_UPPERCASE, SYMBOLS

substitution = Substitution(RU_LOWERCASE + RU_UPPERCASE + SYMBOLS)

phrase = input('Введите фразу (на русском), подлежащую шифрованию: ')
key = input('Введите ключ шифрования (на русском): ')

encrypted_phrase = substitution.encrypt(phrase, key)
print('Зашифрованная фраза:', encrypted_phrase)

decrypted_phrase = substitution.decrypt(encrypted_phrase, key)
