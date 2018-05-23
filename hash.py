from hashlib import md5


def hash_md5(value):
    return md5(value.encode())
