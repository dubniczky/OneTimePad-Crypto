# One-time Pad Cryptography

Simple implementation of the one-time pad encryption algorithm in Python

## Concept

The one-time pad is the definition of a perfectly secure encryption scheme. It uses a random key for all encryption operations and the same key for description. The key, however, does not get used more than once.

Because of this, we generate a larger key than we use to encrypt the message and pre-share this key with both parties. It is then used with an offset to prevent using the same part of the key twice. In such cases, the key could be calculated, because:

$$
c = m \oplus k \\
$$
$$
c' = m' \oplus k \\
$$

this means that

$$
c \oplus c' = m \oplus k \oplus m' \oplus k \\
$$
$$
c \oplus c' = m \oplus m' \oplus k \oplus k \\
$$
$$
c \oplus c' = m \oplus m' \oplus 0 \\
$$
$$
c \oplus c' = m \oplus m' \\
$$

## Usage

### 1. Generate a one-time pad of any length

```bash
python3 generate.py 1024
```

### 2. Encrypt a message using a one-time pad from the 0th offset (the beginning)

```bash
python3 encrypt.py 0
```

2.1 Enter the message when the app asks for it

The ciphertext will be shown after the `=` signs with base64 encoding for easy transfer.

### 3. Decrypt the message

```bash
python3 decrypt.py 0
```

3.1 Enter the cipher when the app asks for it

The initial message will be shown after the `=` signs.

