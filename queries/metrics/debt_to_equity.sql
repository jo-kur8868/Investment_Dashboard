-- Computing Debt-to-Equity Ratio = Total Liability / Shareholder Equity
SELECT
    l.CompanyName,
    l.EndPeriod,
    l.ItemVal AS liabilities,
    e.ItemVal AS equity,
    l.ItemVal * 1.0 / NULLIF(e.ItemVal, 0) AS debt_to_equity
FROM balance_sheet l
JOIN balance_sheet e
ON l.CompanyName = e.CompanyName
AND l.EndPeriod = e.EndPeriod
WHERE l.ItemKey = 'Liabilities'
AND e.ItemKey = 'StockholdersEquity'
AND l.CompanyName = :ticker
AND l.EndPeriod = :end_period