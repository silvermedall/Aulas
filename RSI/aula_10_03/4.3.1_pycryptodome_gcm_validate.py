from Crypto.Cipher import AES
import json

file = input("Ficheiro: ")
key = (
    bytes.fromhex(input("Chave: "))
    or b"(2\x9b\xe9\xde\x89i\xdc\x14\xe2\x8d3-\xea\xdc\xed"
)

with open(file) as f:
    data = json.load(f)

nonce = bytes.fromhex(data["nonce"])
tag = bytes.fromhex(data["tag"])
ciphertext = bytes.fromhex(data["content"])

cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)

try:
    data = cipher.decrypt_and_verify(ciphertext, tag)
    print("Sucesso!")
except ValueError:
    print("Errado!")
