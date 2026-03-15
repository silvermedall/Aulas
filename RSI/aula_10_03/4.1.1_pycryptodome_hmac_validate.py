from Crypto.Hash import HMAC, SHA256
import json

file = input("Ficheiro: ")
key = input("Chave: ").encode() or b"teste"

with open(file, "r") as f:
    hmac = json.loads(f.read())
print("Informação HMAC:\n", hmac)


with open(hmac["file"], "r") as f:
    data = f.read()

mac = HMAC.new(key, digestmod=SHA256)
mac.update(data.encode())
try:
    mac.hexverify(hmac["HMAC"])
    print("Sucesso!")
except ValueError:
    print("Errado!")
