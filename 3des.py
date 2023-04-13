from Cryptodome.Cipher import DES3
from Cryptodome.Random import get_random_bytes

# Chave de 24 bytes (192 bits) para o 3DES
chave = get_random_bytes(24)

# Dados para criptografar
texto_claro = b"Texto a ser criptografado usando o algoritmo 3DES."

# Criação do objeto de cifra 3DES
cipher = DES3.new(chave, DES3.MODE_EAX)

# Criptografa os dados
ciphertext, tag = cipher.encrypt_and_digest(texto_claro)

print("Texto claro:", texto_claro)
print("Texto criptografado:", ciphertext)

# Criação do objeto de decifra 3DES
decipher = DES3.new(chave, DES3.MODE_EAX, cipher.nonce)

# Descriptografa os dados
texto_decifrado = decipher.decrypt_and_verify(ciphertext, tag)

print("Texto decifrado:", texto_decifrado)
