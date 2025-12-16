# Web Scraper + Data Cleaner

## Overview
This project demonstrates a **Python-based web scraping and data cleaning pipeline**.  
It scrapes data from an HTML table, cleans it by removing duplicates and filling missing values, and outputs both a **CSV file** and a **report**.

> **Important Note:** The URL included in the code is for **demonstration purposes only**. It is not a real data source.  
> Replace it with a real website that contains a proper HTML table if you want to scrape actual data. The current sample URL allows you to test the pipeline safely.

---

## Features
- Scrapes tabular data from HTML pages using **BeautifulSoup**
- Cleans data using a modular **clean_data()** function:
  - Removes duplicate rows
  - Fills missing values
- Generates output CSV and a report text file
- All outputs are saved in the `output/` folder
- Handles missing tables gracefully (no crash)

---


---

## Usage

1. **Install dependencies**:
```bash
pip install -r requirements.txt

---
python scraper.py

---

Notes

This project is intended for educational and demonstration purposes.

Be aware of legal and ethical considerations when scraping real websites.

The sample URL in the code is only for testing and demonstration, not for actual data extraction.
