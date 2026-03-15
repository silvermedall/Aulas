from Crypto.Hash import HMAC, SHA256
import json

key = b"teste"
file = input("Ficheiro: ")

with open(file, "r") as f:
    data = f.read()
    print("Mensagem lida:\n", data)


hmac = HMAC.new(key, digestmod=SHA256)
hmac.update(data.encode())

result = json.dumps({"file": file, "HMAC": hmac.hexdigest()})
print("Informação HMAC:\n", result)

newfile = file + ".hmac"
print("Criar ficheiro: " + newfile)
with open(newfile, "w") as f:
    f.write(result)
