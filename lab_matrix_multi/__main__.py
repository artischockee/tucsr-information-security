from lab_matrix_multi.constants import RU_LOWERCASE, RU_UPPERCASE, SYMBOLS
from lab_matrix_multi.matrix_multi import MatrixMulti

matrix_multi = MatrixMulti(RU_LOWERCASE + RU_UPPERCASE + SYMBOLS, SYMBOLS[0])

phrase = input('Введите фразу (на русском), подлежащую шифрованию: ')

encrypted_phrase = matrix_multi.encrypt(phrase)
print('Зашифрованная фраза:', encrypted_phrase)

# decrypted_phrase = matrix_multi.decrypt(encrypted_phrase, key)
# print('Расшифрованная фраза:', decrypted_phrase)
