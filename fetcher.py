import math
import sqlite3
from pathlib import Path
from edgar import set_identity, Company

# Enter your name and your email address
set_identity()

# Establish connection
conn = sqlite3.connect('companies.db')
conn.executescript(Path('queries/schema.sql').read_text())

company_name = 'AAPL'
end_period = 'FY 2025'
income = Company(company_name).income_statement().to_dataframe()
income = income.loc[income['is_abstract'] == False]

entries = []

# Income Statement for FY 2025
for key, val in income[end_period].items():
    if not math.isnan(val):
        entries.append({'CompanyName': company_name, 'EndPeriod': end_period, 'ItemKey': key, 'ItemVal': val})

# Load values into companies.db
conn.executemany(
f"""
INSERT INTO income_statement (CompanyName, EndPeriod, ItemKey, ItemVal)
VALUES (:CompanyName, :EndPeriod, :ItemKey, :ItemVal)
""",
entries,
)

conn.commit()

