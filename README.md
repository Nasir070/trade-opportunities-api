# Trade Opportunities API

FastAPI service for analyzing Indian market sectors and providing AI-powered trade opportunity insights.

# Project Overview

This API provides **AI-generated market insights** for Indian sectors like pharmaceuticals, agriculture, and technology,etc. It fetches live news or data, analyzes it with Google Gemini, and returns a formatted markdown report.

# Features

-  Analyze sectors like "pharmaceuticals", "agriculture", or "technology"
-  AI-generated reports using Gemini or other LLMs
-  Authenticated API access with rate limiting
-  Markdown output format
-  FastAPI with async, modular design
# Tech Stack

- **Framework**: FastAPI (Python)
- **AI Model**: Google Gemini API (or alternate LLMs)
- **Data Source**: Web scraping/APIs (DuckDuckGo, etc.)
- **Storage**: In-memory (no database)
- **Security**: JWT/Guest auth, input validation, rate limiting

# Project Structure

trade-opportunities-api/
├── main.py
├── routes/
│   └── analyze.py
├── services/
│   ├── ai_analysis.py
│   └── data_fetcher.py
├── utils/
│   ├── auth.py
│   └── rate_limiter.py
├── security/
│   └── session.py
├── requirements.txt
└── README.md

# setup
1. Create a virtual environment
  venv\Scripts\activate

2. Install dependencies
  pip install -r requirements.txt

3. Set Up Environment Variables
   GEMINI_API_KEY=your_google_gemini_api_key_here
    API_KEY=trade-api-key-2025

4. Start the FastAPI Development Server
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

   //The server will start at http://localhost:8000

5. Access the API Documentation
    Open your browser and go to:http://localhost:8000/docs(Interactive Swagger UI)

6.  Authorize with Your API Key
    In Swagger UI, click the Authorize button (key icon).

    Enter your API key (from .env, default: trade-api-key-2025).

    Click Authorize.
7. Make an API Request
   In the docs, expand the /api/v1/analyze/{sector} endpoint.

    Click Try it out.

    Type a valid sector (e.g., pharmaceuticals) in the sector field.
    (Allowed sectors: pharmaceuticals, technology, agriculture, automotive, textiles, renewable_energy, banking, telecommunications, manufacturing)

Click Execute.

You will receive a markdown report as the API response

```
