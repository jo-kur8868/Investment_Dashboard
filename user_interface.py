import sqlite3
from pathlib import Path

def main():
    print(" Investment Dashboard ")

    available_metrics = ['working_capital', 'profit_margin', 'return_on_asset', 'return_on_equity']
    metrics_path = 'queries/metrics'
    parameters = {'ticker': 'OSPN', 'end_period': 'FY 2025'}
    
    conn = sqlite3.connect('companies.db')
    cur = conn.execute(Path(f'{metrics_path}/{available_metrics[2]}.sql').read_text(), parameters)
    print(cur.fetchone())

if __name__ == "__main__":
    main()