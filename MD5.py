import hashlib
result=hashlib.md5(b"hello")
result1=hashlib.md5(b"world")
print(f"the byte equivalent of the hash for'Hello'is:{result.digest()}")
print(f"the hexadecimal equivalent of the hash for'Hello'is:{result.hexdigest()}")
print(f"the byte equivalent of the hash for'world'is:{result1.digest()}")
print(f"the hexadecimal equivalent of the hash for'world'is:{result1.hexdigest()}")



