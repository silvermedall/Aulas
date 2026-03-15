# Adaptado de: https://samsclass.info/141/proj/pCH-ECB.htm
# pip install pycryptodome
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
from Crypto.Cipher import AES
key = b'aaaabbbbccccdddd'
cipher = AES.new(key, AES.MODE_ECB)

# Abrir imagem tux: 943,794 bytes
with open("tux.bmp", "rb") as f:
    plain = f.read()

# Remove heading BMP de 64 bytes
# (943794-64)/16 = 58983.125 => (0.125*16 = 2)
# Remover 2 Bytes finais
plain_trimmed = plain[64:-2]

# Encriptação
ciphertext = cipher.encrypt(plain_trimmed)
# Adicionar heading BMP original e final
ciphertext = plain[0:64] + ciphertext + plain[-2:]

# Criar ficheiro encriptado
with open("tux_ecb.bmp", "wb") as f:
    f.write(ciphertext)
