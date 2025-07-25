from fastapi import Request, HTTPException, status
from starlette.middleware.base import BaseHTTPMiddleware
from cachetools import TTLCache
import time, logging

logger = logging.getLogger(__name__)

class RateLimitMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, requests_per_minute: int = 10):
        super().__init__(app)
        self.requests_per_minute = requests_per_minute
        self.cache = TTLCache(maxsize=10000, ttl=60)

    async def dispatch(self, request: Request, call_next):
        if request.url.path in ["/", "/health", "/docs", "/redoc", "/openapi.json"]:
            return await call_next(request)
        client_id = request.headers.get("X-API-KEY") or request.client.host
        current_min = int(time.time() / 60)
        key = f"{client_id}:{current_min}"
        count = self.cache.get(key, 0)
        if count >= self.requests_per_minute:
            logger.warning(f"Rate limit exceeded for {client_id}")
            raise HTTPException(status_code=status.HTTP_429_TOO_MANY_REQUESTS, detail="Rate limit exceeded.")
        self.cache[key] = count + 1
        response = await call_next(request)
        response.headers["X-RateLimit-Limit"] = str(self.requests_per_minute)
        response.headers["X-RateLimit-Remaining"] = str(max(0, self.requests_per_minute - (count + 1)))
        return response
