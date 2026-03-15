from Crypto.Hash import CMAC
from Crypto.Cipher import AES
import json

file = input("Ficheiro: ")
key = input("Chave: ").encode() or b"1234567890123456"

with open(file, "r") as f:
    cmac = json.loads(f.read())
print("Informação CMAC:\n", cmac)


with open(cmac["file"], "r") as f:
    data = f.read()

mac = CMAC.new(key, ciphermod=AES)
mac.update(data.encode())
try:
    mac.hexverify(cmac["CMAC"])
    print("Sucesso!")
except ValueError:
    print("Errado!")
