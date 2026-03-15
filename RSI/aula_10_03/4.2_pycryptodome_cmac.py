from Crypto.Hash import CMAC
from Crypto.Cipher import AES
import json

key = b"1234567890123456"
file = input("Ficheiro: ")

with open(file, "r") as f:
    data = f.read()

cmac = CMAC.new(key, ciphermod=AES)
cmac.update(data.encode())

result = json.dumps({"file": file, "CMAC": cmac.hexdigest()})
print("Informação CMAC:\n", result)

newfile = file + ".cmac"
print("Criar ficheiro: " + newfile)
with open(newfile, "w") as f:
    f.write(result)
