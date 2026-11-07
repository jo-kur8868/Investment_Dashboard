import os
import math
import sqlite3
import pandas as pd
from pathlib import Path
from edgar import set_identity, Company, use_local_storage, download_filings

# List of companies to be fetched and stored
company_list = ['CRTO', 'OSPN', 'ADBE', 'SD']

# Caching and returning dataframes of statements
def get_statement(ticker):
    os.makedirs('cache/financials', exist_ok=True)
    cache_dir = Path('cache/financials')

    statements = ['income_statement', 'balance_sheet', 'cash_flow']
    result = []
    for i in range(len(statements)):
        path = cache_dir / f'{ticker}_{statements[i]}.pkl'

        if path.exists():
            result.append(pd.read_pickle(path))
        else:
            match(i):
                case 0:
                    df = Company(ticker).income_statement().to_dataframe()
                    df.to_pickle(path)
                    result.append(df)
                case 1:
                    df = Company(ticker).balance_sheet().to_dataframe()
                    df.to_pickle(path)
                    result.append(df)
                case 2:
                    df = Company(ticker).cash_flow_statement().to_dataframe()
                    df.to_pickle(path)
                    result.append(df)

    return result

# Get filing forms and cache 
def get_latest_filing(ticker, form):
    os.makedirs('cache/filing_library', exist_ok=True)
    cache_dir = Path('cache/filing_library')

    path = cache_dir / f'{ticker}_{form}.md'

    if path.exists():
        return path.read_text(encoding='utf-8')
    
    filing = Company(ticker).get_filings(form=form).latest().markdown()
    path.write_text(filing, encoding='utf-8')
    return filing

# Getting entries fetched from Edgar
def get_entries(statement, company_name, end_period):
    entries = []
    statement = statement.loc[statement['is_abstract'] == False]
    for key, val in statement[end_period].items():
        if not math.isnan(val):
            entries.append({'CompanyName': company_name, 
                            'EndPeriod': end_period, 
                            'ItemKey': key, 
                            'ItemVal': val})
    return entries

# Load entries into companies.db
def load_entries(connection, statement, entries):
    connection.executemany(
    f'''
    INSERT INTO {statement} (CompanyName, EndPeriod, ItemKey, ItemVal)
    VALUES (:CompanyName, :EndPeriod, :ItemKey, :ItemVal)
    ON CONFLICT(CompanyName, EndPeriod, ItemKey) DO NOTHING
    ''',
    entries,
    )

def main():
    # Create a text file with your_name your_email@tag.com
    with open('information.txt', 'r') as file:
        name = file.read()

    # Enter your name and your email address
    set_identity(name)

    # Establish connection
    conn = sqlite3.connect('companies.db')
    conn.executescript(Path('queries/schema.sql').read_text())

    for company in company_list:
        year = 2025
        company_name = company
        periods = [f'FY {year}', f'FY {year-1}',f'FY {year-2}', f'FY {year-3}']

        # Get 10-Q
        get_latest_filing(company_name, '10-Q')

        # Get 10-K
        get_latest_filing(company_name, '10-K')

        # Financial Statements
        financial_stmts = get_statement(company_name)

        # Each FY year in the financials
        for end_period in periods:
            # Income Statement
            income_entries = get_entries(financial_stmts[0], company_name, end_period)
            load_entries(conn, 'income_statement', income_entries)

            # Financial Position
            balance_entries = get_entries(financial_stmts[1], company_name, end_period)
            load_entries(conn, 'balance_sheet', balance_entries)

            # Cash Flow Statement
            cash_flow_entries = get_entries(financial_stmts[2], company_name, end_period)
            load_entries(conn, 'cash_flow', cash_flow_entries)

        conn.commit()

if __name__ == '__main__':
    main()