from fastapi import HTTPException, Security, status
from fastapi.security import APIKeyHeader
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY_NAME = "X-API-KEY"
api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)
DEFAULT_API_KEY = os.getenv("API_KEY", "trade-api-key-2025")

async def get_api_key(api_key: str = Security(api_key_header)):
    if not api_key or api_key != DEFAULT_API_KEY:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid or missing API key", headers={"WWW-Authenticate": "ApiKey"})
    return api_key

def validate_sector_input(sector: str) -> str:
    allowed = ['pharmaceuticals', 'technology', 'agriculture', 'automotive', 'textiles', 'renewable_energy', 'banking', 'telecommunications', 'manufacturing']
    sector_clean = sector.lower().strip()
    if sector_clean not in allowed:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"Invalid sector. Allowed sectors: {', '.join(allowed)}")
    return sector_clean
