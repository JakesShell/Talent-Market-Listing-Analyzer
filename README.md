# Talent Market Listing Analyzer

## Overview

Talent Market Listing Analyzer is a Python-based utility for parsing local HTML exports of job listings and converting them into structured CSV output for hiring market review.

This project is positioned as a recruiter-ready Python portfolio piece. It upgrades a simple web scraper concept into a more practical business-facing analysis tool that better fits recruiting operations, market research, talent intelligence, and hiring trend review workflows.

## Real-World Business Use Case

This project maps to practical workflows used by:

- Recruiting Operations Teams
- Talent Intelligence Workflows
- Hiring Market Research
- Workforce Planning Support
- Python Data Utility Development

A team may need to answer questions such as:

- Which roles are appearing most often in a job export?
- Which companies are hiring in specific markets?
- Which locations show the strongest activity?
- How can job listing data be turned into a structured CSV for review?

This utility is useful for local listing analysis, CSV generation, and portfolio demonstration of turning a fragile scraping concept into a cleaner market-analysis workflow.

## Key Features

- Local HTML Listing Parsing
- Structured Title, Company, And Location Extraction
- CSV Export
- Listing Summary Output
- Company And Location Counts
- Lightweight Python CLI Workflow

## Tech Stack

- Python
- BeautifulSoup
- pandas

## Repository Contents

- `MarketListingAnalyzer.py`
- `requirements.txt`
- `sample_job_board.html`
- `README.md`
- `.gitignore`

## How To Run

### 1. Install Dependencies

```powershell
pip install -r requirements.txt
