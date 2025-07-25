from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.responses import PlainTextResponse
from app.security import get_api_key, validate_sector_input
from app.data_collection import DataCollector
from app.analysis import AIAnalyzer
import logging, uuid

logger = logging.getLogger(__name__)
router = APIRouter()
data_collector = DataCollector()
ai_analyzer = AIAnalyzer()

@router.get("/analyze/{sector}", response_class=PlainTextResponse, summary="Analyze sector for trade opportunities", description="Generate comprehensive trade opportunity analysis for specified Indian sector")
async def analyze_sector(sector: str, api_key: str = Depends(get_api_key)):
    try:
        sector_clean = validate_sector_input(sector)
        request_id = str(uuid.uuid4())[:8]
        logger.info(f"Processing analysis request for sector: {sector_clean}, ID: {request_id}")
        news_data = await data_collector.fetch_sector_news(sector_clean)
        market_data = await data_collector.fetch_market_data(sector_clean)
        analysis_report = await ai_analyzer.analyze_sector(sector_clean, news_data, market_data)
        return analysis_report
    except HTTPException:
        raise
    except Exception as e:
        logger.error(f"Unexpected error in sector analysis: {str(e)}")
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail="Internal server error occurred during analysis")

@router.get("/sectors", summary="List available sectors", description="Get list of all available sectors for analysis")
async def list_sectors(api_key: str = Depends(get_api_key)):
    sectors = [
        'pharmaceuticals', 'technology', 'agriculture', 'automotive', 'textiles',
        'renewable_energy', 'banking', 'telecommunications', 'manufacturing'
    ]
    return {"available_sectors": sectors, "total_count": len(sectors), "usage": "Use any sector name with /analyze/{sector} endpoint"}
