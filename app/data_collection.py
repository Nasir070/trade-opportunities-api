from duckduckgo_search import DDGS
from typing import List, Dict
from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class DataCollector:
    def __init__(self):
        self.ddgs = DDGS()

    async def fetch_sector_news(self, sector: str, max_results: int = 10) -> List[Dict]:
        try:
            query = f"{sector} India market trends news 2025"
            results = []
            for r in self.ddgs.text(keywords=query, region='in-en', safesearch='moderate', timelimit='m', max_results=max_results):
                results.append({'title': r.get('title', ''), 'snippet': r.get('body', ''), 'url': r.get('href', ''), 'date': datetime.now().isoformat()})
            return results
        except Exception as e:
            logger.error(f"Error fetching sector news: {e}")
            return []

    async def fetch_market_data(self, sector: str) -> Dict:
        try:
            queries = [f"{sector} India stock market performance", f"{sector} India export import data", f"{sector} India government policy"]
            indicators = []
            for q in queries:
                for r in self.ddgs.text(keywords=q, region='in-en', safesearch='moderate', timelimit='w', max_results=3):
                    indicators.append(r)
            return {'market_indicators': indicators, 'search_timestamp': datetime.now().isoformat()}
        except Exception as e:
            logger.error(f"Error fetching market data: {e}")
            return {'market_indicators': [], 'search_timestamp': datetime.now().isoformat()}
