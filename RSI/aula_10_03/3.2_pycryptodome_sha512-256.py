from Crypto.Hash import SHA512

msg = input("Message: ").encode("utf-8")
h5 = SHA512.new()
h5.update(msg)

h5_2 = SHA512.new(truncate="256")
h5_2.update(msg)

print("SHA512: ", h5.hexdigest())
print("SHA256/512: ", h5_2.hexdigest())
