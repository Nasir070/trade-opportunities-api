# clone the Repository
 git clone  https://github.com/Nasir070/trade-opportunities-api.git

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



<img width="2391" height="1131" alt="Screenshot 2025-07-25 190623" src="https://github.com/user-attachments/assets/31cd5f0c-bcdb-4e35-ba45-20d9b7138b85" />
<img width="2280" height="1184" alt="Screenshot 2025-07-25 190649" src="https://github.com/user-attachments/assets/e075a060-1043-4cd1-bebb-b7e85371194f" />

