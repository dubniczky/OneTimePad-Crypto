import sys
import base64


pad_file = "secrets/onetimepad.txt"



def import_pad():
    with open(pad_file, "r") as f:
        pad = f.read()
    return base64.b64decode(pad)

def encrypt(message, pad, offset=0):
    return bytes([message[i] ^ pad[(i + offset) % len(pad)] for i in range(len(message))])

def encode(cipher):
    return base64.b64encode(cipher).decode("utf-8")


# Require an offset
if len(sys.argv) < 2:
    print("Usage: python3 encrypt.py <offset>")
    exit(1)
offset = int(sys.argv[1])
print(f'Using offset: {sys.argv[1]}')

message = input("Message: ")

print(f'Importing pad from: {pad_file}')
pad = import_pad()
print(f'Imported pad of: {len(pad)} bytes')
enc = encrypt(message.encode('utf-8'), pad)
encstring = encode(enc)

print(f'{"="*16}')
print(encstring)
