from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import logging
from app.api import router
from app.rate_limit import RateLimitMiddleware
from app.utils import setup_logging

setup_logging()
logger = logging.getLogger(__name__)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Starting Trade Opportunities API")
    yield
    logger.info("Shutting down Trade Opportunities API")

app = FastAPI(
    title="Trade Opportunities API",
    description="Market data and trade opportunity analysis for Indian sectors using AI",
    version="1.0.0",
    lifespan=lifespan,
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.add_middleware(RateLimitMiddleware)
app.include_router(router, prefix="/api/v1")

@app.get("/")
async def root():
    return {"message": "Trade Opportunities API", "version": "1.0.0", "documentation": "/docs"}

@app.get("/health")
async def health_check():
    return {"status": "healthy", "service": "trade-opportunities-api"}
