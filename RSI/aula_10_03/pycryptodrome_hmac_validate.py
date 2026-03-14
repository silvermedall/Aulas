from Crypto.Hash import HMAC, SHA256
import json

file = input("Ficheiro: ")

with open(file, "r") as f:
    hmac = json.loads(f.read())
print("Informação HMAC:\n", hmac)

key = input("Chave: ").encode()

with open(hmac["file"], "r") as f:
    data = f.read()

mac = HMAC.new(key, digestmod=SHA256, msg=data.encode())
try:
    mac.hexverify(hmac["HMAC"])
    print("Sucesso!")
except ValueError:
    print("Errado!")
