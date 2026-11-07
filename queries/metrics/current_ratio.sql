-- Computing the Current Ratio = Current Assets / Current Liabilities
SELECT
    ca.CompanyName,
    ca.EndPeriod,
    ca.ItemVal AS current_assets,
    cl.ItemVal AS current_liabilities,
    ca.ItemVal * 1.0 / NULLIF(cl.ItemVal, 0) AS current_ratio
FROM balance_sheet ca
JOIN balance_sheet cl
ON ca.CompanyName = cl.CompanyName
AND ca.EndPeriod = cl.EndPeriod
WHERE ca.ItemKey = 'AssetsCurrent'
AND cl.ItemKey = 'LiabilitiesCurrent'
AND ca.CompanyName = :ticker
AND ca.EndPeriod = :end_period;