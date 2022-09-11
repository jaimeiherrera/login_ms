from fastapi import FastAPI

import jwt

app = FastAPI()


@app.get("/test")
def test():
    jwt
    return None


@app.get("/")
def root():
    return {"message": "Welcome to login_ms!"}
