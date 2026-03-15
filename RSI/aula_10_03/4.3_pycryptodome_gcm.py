from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import json

key = get_random_bytes(16)
print(key)
file = input("Ficheiro: ")

with open(file, "r") as f:
    data = f.read()

gcm = AES.new(key, AES.MODE_GCM)
ciphertext, tag = gcm.encrypt_and_digest(data.encode())

result = json.dumps(
    {
        "file": file,
        "nonce": gcm.nonce.hex(),
        "tag": tag.hex(),
        "content": ciphertext.hex(),
    }
)
print("Informação CMAC:\n", result)

newfile = file + ".gcm"
print("Criar ficheiro: " + newfile)
with open(newfile, "w") as f:
    f.write(result)
