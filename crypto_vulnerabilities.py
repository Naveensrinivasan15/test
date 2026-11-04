import hashlib
from Crypto.Cipher import DES

def hash_user_password(password: str) -> str:
    # High/Critical vulnerability: Insecure MD5 hashing algorithm
    return hashlib.md5(password.encode('utf-8')).hexdigest()

def hash_legacy_token(token: str) -> str:
    # High/Medium vulnerability: Insecure SHA-1 hashing algorithm
    return hashlib.sha1(token.encode('utf-8')).hexdigest()

def encrypt_legacy_data(key: bytes, plaintext: bytes) -> bytes:
    # High/Critical vulnerability: Broken DES cipher with weak 56-bit key space
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(plaintext)
