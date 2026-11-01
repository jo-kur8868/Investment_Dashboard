# Investment Dashboard

A Python-based research tool for collecting and organizing public company financial data from SEC EDGAR filings. The project is designed to help with investment analysis by downloading company statements, caching annual reports, and storing structured financial metrics in a local SQLite database for ongoing review.

## Overview

This repository pulls financial statement data for a company (such as income statements, balance sheets, and cash flow statements), stores the results locally, and makes it easier to compute key metrics like profit margins and return ratios. It is built for personal investing research and can be extended to track multiple companies over time.

## What the project does

- Downloads financial statement data from SEC EDGAR using the `edgar` library
- Saves statement tables in a local cache folder for faster repeated access
- Stores selected filing data in `companies.db`
- Downloads and preserves 10-K filings in `filing_library/`
- Runs SQL-based metric queries for analysis
- Provides a lightweight dashboard entry point for quick metric checks

## Project structure

- `fetcher.py` — main data ingestion script that retrieves financial statements and 10-K filings, and loads them into SQLite
- `user_interface.py` — simple console interface that runs a sample SQL metric query against the database
- `queries/schema.sql` — SQLite schema for storing statement data
- `queries/metrics.sql` — example metrics and analytical SQL queries
- `cache/` — cached statement data stored as pickled pandas DataFrames
- `filing_library/` — saved 10-K markdown files
- `companies.db` — local SQLite database created by the project
- `information.txt` — SEC EDGAR identity information required by the library
- `.gitignore` — excludes local cache and generated data files from version control

## Data flow

1. The project reads the company ticker and filing period from code.
2. `fetcher.py` fetches the latest financial statements from the SEC EDGAR data source.
3. Statements are cached locally in `cache/` to avoid repeated downloads.
4. The latest 10-K filing is downloaded and saved as Markdown in `filing_library/`.
5. Each statement item is inserted into SQLite tables organized by:
   - `income_stmt`
   - `balance_sheet`
   - `cash_flow`
6. SQL queries in `queries/metrics.sql` can be used to calculate ratios such as net margin and other fundamental metrics.

## Database schema

The schema is defined in `queries/schema.sql` and creates the following tables:

- `income_stmt`
- `balance_sheet`
- `cash_flow`

Each table stores:

- `CompanyName`
- `EndPeriod`
- `ItemKey`
- `ItemVal`

The primary key is a combination of company name, period, item name, and value to prevent duplicate rows.

## Example metrics

The project includes sample queries for business ratios, including:

- Net profit margin
- Return on equity
- Return on assets
- Working capital
- Retained earnings

The metric SQL is intentionally easy to extend as you build a broader investment research workflow.

## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/jo-kur8868/Investment_Dashboard.git
   cd Investment_Dashboard
   ```

2. Create and activate a virtual environment if desired:

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

3. Install the dependencies:

   ```bash
   pip install pandas edgar
   ```

4. Update `information.txt` with your name and email address so the SEC EDGAR client can identify your access properly.

5. Run the fetcher:

   ```bash
   python fetcher.py
   ```

## Usage

### Fetch financial data

```bash
python fetcher.py
```

This script:

- creates the SQLite database if needed
- loads the schema
- downloads statement data and 10-K files
- inserts entries into the database

### Query the database

```bash
python user_interface.py
```

This script executes a sample SQL query from `queries/metrics.sql` against the local `companies.db` file and prints the result.

## Notes

- This project is intended for personal research, education, and analysis support.
- Data comes from public SEC filings and may be refreshed or recalculated depending on the company and reporting cycle.
- It is a lightweight local research tool rather than a full-featured financial application or advisory system.
- The code is easy to extend for additional companies, ratios, comparison tables, and visualization.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
