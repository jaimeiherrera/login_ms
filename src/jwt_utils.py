import jwt
from decouple import config


def encode_jwt() -> str:
    return jwt.encode({"some": "payload"}, config("SECRET"), algorithm=config("ALGORITHM"))


def decode_jwt(encoded_jwt: str) -> str:
    return jwt.decode(encoded_jwt, config("SECRET"), algorithms=[config("ALGORITHM")])
