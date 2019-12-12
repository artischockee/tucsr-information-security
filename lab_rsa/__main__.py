from lab_rsa.constants import EN_LOWERCASE, EN_UPPERCASE, RU_LOWERCASE, RU_UPPERCASE, SYMBOLS
from lab_rsa.rsa import Rsa

rsa = Rsa(EN_LOWERCASE + EN_UPPERCASE + RU_LOWERCASE + RU_UPPERCASE + SYMBOLS)

phrase = input('Введите фразу, подлежащую шифрованию: ')

[encrypted_phrase, public_key, private_key] = rsa.encrypt(phrase)
print('Зашифрованная фраза:', encrypted_phrase)
print('Публичный ключ:', public_key)
print('Приватный ключ:', private_key)

decrypted_phrase = rsa.decrypt(encrypted_phrase, private_key)
print('Расшифрованная фраза:', decrypted_phrase)
