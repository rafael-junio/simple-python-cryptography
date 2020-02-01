import os
import pickle
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
print('Type your password: ')
aad = input()
aad = aad.encode()

with open('objs.pkl', 'rb') as f:
    key, chacha, nonce, ct = pickle.load(f)
print('Your secrets: ')
print(chacha.decrypt(nonce, ct, aad))
