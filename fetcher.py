from edgar import set_identity, Company
import os
import pandas as pd

# Enter your name and your email address
set_identity()

# Cache directory
Cache_DIR = "cache"
os.makedirs(Cache_DIR, exist_ok=True)

ticker = 'AAPL'
cache_file = os.path.join(Cache_DIR, f'{ticker.lower()}_income_statement.csv')

if os.path.exists(cache_file):
    df = pd.read_csv(cache_file)
else:
    company = Company('AAPL')
    income_stmt = company.get_financials().income_statement()
    df = income_stmt.to_dataframe()
    df.to_csv(cache_file, index=False)



