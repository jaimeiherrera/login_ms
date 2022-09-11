from fastapi import FastAPI

from .jwt_utils import decode_jwt, encode_jwt

app = FastAPI()


@app.get("/test")
def test():
    encoded = encode_jwt()
    decoded = decode_jwt(encoded)
    return None


@app.get("/")
def root():
    return {"message": "Welcome to login_ms!"}
