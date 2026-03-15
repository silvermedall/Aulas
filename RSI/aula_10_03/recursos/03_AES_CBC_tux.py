# pip install pycryptodome
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
from Crypto.Cipher import AES
key = b"aaaabbbbccccdddd"
iv = b"0000111122223333"
cipher = AES.new(key, AES.MODE_CBC, iv)

# Abrir imagem tux: 943,794 bytes
with open("tux.bmp", "rb") as f:
    clear = f.read()

# Remove heading BMP de 64 bytes
# (943794-64)/16 = 58983.125 => (0.125*16 = 2)
# Remover 2 Bytes finais
clear_trimmed = clear[64:-2]

# Encriptação
ciphertext = cipher.encrypt(clear_trimmed)
# Adicionar heading BMP original e final
ciphertext = clear[0:64] + ciphertext + clear[-2:]

# Criar ficheiro encriptado
with open("tux_cbc.bmp", "wb") as f:
    f.write(ciphertext)
