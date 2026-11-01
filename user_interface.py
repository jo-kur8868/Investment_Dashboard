import sqlite3
from pathlib import Path

def main():
    print(" Investment Dashboard ")

    conn = sqlite3.connect('companies.db')
    cur = conn.execute(Path('queries/metrics.sql').read_text(), {'ticker': 'OSPN', 'end_period': 'FY 2025'})
    print(cur.fetchone()[-1]*100)

if __name__ == "__main__":
    main()