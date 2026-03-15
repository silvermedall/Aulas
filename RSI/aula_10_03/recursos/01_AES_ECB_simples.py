# pip install pycryptodome
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ecb-mode
from Crypto.Cipher import AES
from base64 import b64encode, b64decode
# Definição da chave: 16 Bytes, 24 ou 32 bytes para AES-128 AES-192 ou AES-256
key = b'aaaabbbbccccddddaaaabbbbccccdddd'
# Criação do objeto de encriptação com o modo ECB
cipher = AES.new(key, AES.MODE_ECB)

# Ler Mensagem e converter para Base64 (por causa dos caracteres especiais)
user_input = input('Mensagem..: ')
plaintext = user_input.encode()

# Criar string com comprimento múltiplo do tamanho do bloco PKCS#7
BLOCK_SIZE = 16
padding_length = BLOCK_SIZE - (len(plaintext) % BLOCK_SIZE)
plaintext += bytes([padding_length]) * padding_length

# Encriptar mensagem
ciphertext = cipher.encrypt(plaintext)
print('Ciphertext (Base64):', b64encode(ciphertext).decode())

# Desencriptar mensagem
decrypted = cipher.decrypt(ciphertext)
original = decrypted[:-padding_length].decode()
print('Original:', original)
