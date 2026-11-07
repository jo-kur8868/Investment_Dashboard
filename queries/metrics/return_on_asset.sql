/* Return on Assets = Net Income / Avg Total Assets */
SELECT
    ni.CompanyName,
    ni.EndPeriod,
    ni.ItemVal AS net_income,
    asst.ItemVal As assets,
    ni.ItemVal * 100.0 / NULLIF(asst.ItemVal, 0) AS roa
FROM income_statement ni
JOIN balance_sheet asst
ON ni.CompanyName = asst.CompanyName
AND ni.EndPeriod = ni.EndPeriod
WHERE ni.ItemKey = 'NetIncomeLoss'
AND asst.ItemKey = 'Assets'
AND ni.CompanyName = :ticker
AND ni.EndPeriod = :end_period;