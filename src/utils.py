import hashlib

import jwt
from decouple import config


def encoder(str_to_encode: str) -> str:
    """Encode str with sha256 algorithm

    Args:
        str_to_encode (str): str to be hashed

    Returns:
        str: str hashed
    """
    return hashlib.sha256(str_to_encode.encode()).hexdigest()


def encode_jwt() -> str:
    return jwt.encode({"some": "payload"}, config("SECRET"), algorithm=config("ALGORITHM"))


def decode_jwt(encoded_jwt: str) -> str:
    return jwt.decode(encoded_jwt, config("SECRET"), algorithms=[config("ALGORITHM")])
