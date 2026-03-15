from Crypto.Hash import MD2, MD5

msg = input("Message: ").encode("utf-8")
h2 = MD2.new()
h5 = MD5.new()

h2.update(msg)
h5.update(msg)

print("MD2: ", h2.hexdigest())
print("MD5: ", h5.hexdigest())
