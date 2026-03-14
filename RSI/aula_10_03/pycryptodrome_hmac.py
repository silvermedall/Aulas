from Crypto.Hash import HMAC, SHA256
import json

file = input("Ficheiro: ")

with open(file, "r") as f:
    data = f.read()
    print("Mensagem lida:\n", data)

key = b"teste"

mac = HMAC.new(key, digestmod=SHA256, msg=data.encode())

result = json.dumps({"file": file, "HMAC": mac.hexdigest()})
print("Informação HMAC:\n", result)

newfile = file + ".hmac"
print("Criar ficheiro: " + newfile)
with open(newfile, "w") as f:
    f.write(result)
