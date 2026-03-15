# pip install pycryptodome
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ctr-mode
from Crypto.Cipher import AES
from base64 import b64decode
import json

key = b"abcd1234abcd1234"


# Abrir Ficheiro JSON
with open("msg_enc.json", "r") as f:
    data = json.loads(f.read())


# Obter dados da encriptação
nonce = b64decode(data["nonce"])
ct = b64decode(data["ciphertext"])
# Desencriptar
cipher = AES.new(key, AES.MODE_CTR, nonce=nonce)
msg = cipher.decrypt(ct)

# Apresentar mensagem
print("Mensagem:\n", msg.decode())
