from Crypto.Hash import SHA256, SHA512

msg = input().encode("utf-8")
h2 = SHA256.new()
h5 = SHA512.new()

h2.update(msg)
h5.update(msg)

print("Message: ", msg)
print("SHA256: ", h2.hexdigest())
print("SHA512: ", h5.hexdigest())
