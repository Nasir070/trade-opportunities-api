from pydantic import BaseModel, validator
from typing import Optional
from datetime import datetime

class AnalysisRequest(BaseModel):
    sector: str
    @validator('sector')
    def validate_sector(cls, v):
        allowed = ['pharmaceuticals', 'technology', 'agriculture', 'automotive', 'textiles', 'renewable_energy', 'banking', 'telecommunications', 'manufacturing']
        if v.lower() not in allowed:
            raise ValueError(f"Sector must be one of: {', '.join(allowed)}")
        return v.lower()

class AnalysisResponse(BaseModel):
    sector: str
    report: str
    generated_at: datetime
    request_id: Optional[str] = None

class ErrorResponse(BaseModel):
    error: str
    message: str
    status_code: int
