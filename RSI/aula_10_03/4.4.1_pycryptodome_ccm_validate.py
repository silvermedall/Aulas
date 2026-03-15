from Crypto.Cipher import AES
import json

file = input("Ficheiro: ")
key = bytes.fromhex(input("Chave: ")) or b"Qb\xfa9O_\xd8Ql\x8bSk\xeaL\xa4\xd3"

with open(file) as f:
    data = json.load(f)

nonce = bytes.fromhex(data["nonce"])
tag = bytes.fromhex(data["tag"])
ciphertext = bytes.fromhex(data["content"])

cipher = AES.new(key, AES.MODE_CCM, nonce=nonce)

try:
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print("Sucesso!")
except ValueError:
    print("Errado!")
