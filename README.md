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
- `queries/metrics/` — one parameterized SQL query per metric
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
6. Individual SQL queries in `queries/metrics/` calculate metrics such as net margin and other fundamental metrics. The interface loads and runs only the selected metric.

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

The project includes one SQL file per metric:

- `queries/metrics/profit_margin.sql` — net profit margin
- `queries/metrics/return_on_equity.sql` — return on equity
- `queries/metrics/return_on_asset.sql` — return on assets
- `queries/metrics/working_capital.sql` — working capital

Each query accepts `:ticker` and `:end_period` parameters. Keeping metrics in separate files lets the application execute only the metric needed; it does not calculate the other metrics. Add a new metric by creating another single-statement SQL file in this directory.

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

This script selects a metric from `queries/metrics/`, executes only that SQL query against the local `companies.db`, and prints its result. The selected query receives the ticker and period specified in `user_interface.py`.

## Notes

- This project is intended for personal research, education, and analysis support.
- Data comes from public SEC filings and may be refreshed or recalculated depending on the company and reporting cycle.
- It is a lightweight local research tool rather than a full-featured financial application or advisory system.
- The code is easy to extend for additional companies, ratios, comparison tables, and visualization.

## License

This project is licensed under the MIT License. See `LICENSE` for details.
