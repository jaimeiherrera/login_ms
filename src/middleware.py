from multiprocessing import Process

from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

from .logger import Log


class RequestMiddleware(BaseHTTPMiddleware):
    def __init__(self, app):
        super().__init__(app)

    async def dispatch(self, request: Request, call_next):
        message = "API Requested."
        Process(target=Log().write_log, args=(message,)).start()

        return await call_next(request)
