# One-time Pad Cryptography

Simple implementation of the one-time pad encryption algorithm in Python

## Concept

The one-time pad is the definition of a perfectly secure encryption scheme. It uses a random key for all encryption operations and the same key for description. The key, however, does not get used more than once.

Because of this, we generate a larger key than we use to encrypt the message and pre-share this key with both parties. It is then used with an offset to prevent using the same part of the key twice. In such cases, the key could be calculated, because:

$$
c = m \oplus k \\
c' = m' \oplus k \\
$$

this means that

$$
c \oplus c' = m \oplus k \oplus m' \oplus k \\
c \oplus c' = m \oplus m' \oplus k \oplus k \\
c \oplus c' = m \oplus m' \oplus 0 \\
c \oplus c' = m \oplus m' \\
$$
