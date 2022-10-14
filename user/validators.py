import bcrypt


def hash_password(value: str) -> bytes:
    return bcrypt.hashpw(value.encode("utf-8"), bcrypt.gensalt())
