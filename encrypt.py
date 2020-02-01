import os
import pickle
from cryptography.hazmat.primitives.ciphers.aead import ChaCha20Poly1305
print('Type your secrets...')
segredos = input()
data = segredos.encode()

print('Type your password to encrypt your secrets: ')
password = input()
aad = password.encode()

key = ChaCha20Poly1305.generate_key()
chacha = ChaCha20Poly1305(key)
nonce = os.urandom(12)
ct = chacha.encrypt(nonce, data, aad)

with open('objs.pkl', 'wb') as f:  
    pickle.dump([key, chacha, nonce, ct], f)
print('Secrets saved, please save the objs.pkl in a safe place.')