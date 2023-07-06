import sys
import os
import base64


file = "secrets/onetimepad.txt"
size = 1024


if len(sys.argv) > 1:
    size = int(sys.argv[1])
    
print(f"Generating file of size: {size} bytes")

rand = os.urandom(size)
encoded = base64.b64encode(rand)

with open(file, "w") as f:
    f.write(encoded.decode("utf-8"))
