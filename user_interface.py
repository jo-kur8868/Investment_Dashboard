import sqlite3
import streamlit as st
from pathlib import Path

_metrics_path = 'queries/metrics'

def get_metric(conn, metric, ticker, year):
    parameters = {'ticker': ticker, 'end_period': f'FY {year}'}
    cur = conn.execute(Path(f'{_metrics_path}/{metric}.sql').read_text(), parameters)
    return cur.fetchone()[-1]
    

def main():
    st.write(' Investment Dashboard ')

    # Establish connection to db
    conn = sqlite3.connect('companies.db')

    available_metrics = [
        'working_capital', 'profit_margin', 'return_on_asset', 'return_on_equity', 'current_ratio',
        'debt_to_equity'
        ]

    # Metrics Showcase
    metric_string = 'VIEW METRICS: '
    for metric in available_metrics:
        metric_string = f'{metric_string} | {metric}'
    metric_string = f'{metric_string} |'
    st.write(metric_string)

    # Get ticker and year
    ticker = st.text_input('Enter ticker: ')
    year = st.text_input('Enter year: ')

    choice = st.text_input('Enter your choice: ')
    match(choice):
        case m if m == available_metrics[0]:
            st.write(get_metric(conn, m, ticker, year))
        case n if n == available_metrics[1]:
            st.write(get_metric(conn, n, ticker, year)) 
        case o if o == available_metrics[2]:
            st.write(get_metric(conn, n, ticker, year)) 
        case p if p == available_metrics[3]:
            st.write(get_metric(conn, n, ticker, year)) 
        case q if q == available_metrics[4]:
            st.write(get_metric(conn, n, ticker, year)) 
        case r if r == available_metrics[5]:
            st.write(get_metric(conn, n, ticker, year)) 
        case _ :
            st.write('Please enter a valid choice.')

if __name__ == "__main__":
    main()