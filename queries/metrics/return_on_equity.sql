/* Return on Equity = Net Income / Avg Total Shareholder Equity */
SELECT
    ni.CompanyName,
    ni.EndPeriod,
    ni.ItemVal AS net_income,
    eq.ItemVal As equity,
    ni.ItemVal * 1.0 / NULLIF(eq.ItemVal, 0) AS roe
FROM income_stmt ni
JOIN balance_sheet eq
ON ni.CompanyName = eq.CompanyName
AND ni.EndPeriod = ni.EndPeriod
WHERE ni.ItemKey = 'NetIncomeLoss'
AND eq.ItemKey = 'StockholdersEquity'
AND ni.CompanyName = :ticker
AND ni.EndPeriod = :end_period;