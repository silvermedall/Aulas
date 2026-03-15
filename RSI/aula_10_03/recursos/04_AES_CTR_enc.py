# pip install pycryptodome
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/aes.html
# https://pycryptodome.readthedocs.io/en/latest/src/cipher/classic.html#ctr-mode
from Crypto.Cipher import AES
from base64 import b64encode
import json

key = b"abcd1234abcd1234"
cipher = AES.new(key, AES.MODE_CTR)

# Ler ficheiro
with open("msg.txt", "r") as f:
    data = f.read()
print('Mensagem lida:\n', data)

# Encriptar
ciphertext = cipher.encrypt(data.encode())
# Obter nonce gerado automaticamente na encriptação
nonce = b64encode(cipher.nonce).decode()
# Obter encriptação como texto para guardar no ficheiro
ct = b64encode(ciphertext).decode()
# Criar JSON com resultado
result = json.dumps({'nonce': nonce, 'ciphertext': ct})
print('Mensagem a criar:\n', result)

# Escrever ficheiro
with open("msg_enc.json", "w") as f:
    f.write(result)
