1. Create two separate file: (1) encrypt and (2) decrypt
2. The file is an input to encrypt, which is either saves the encrypted file locally or sends it via socket
3. Password input for password
4. PDKDF2 (Password based derivtion function) with SHA-512 algorithm with 4096 iterations; select salt string
5. encryption is AES128 CBC mode, IV on5844 each "5844"
6. HMAC hash appended to the data