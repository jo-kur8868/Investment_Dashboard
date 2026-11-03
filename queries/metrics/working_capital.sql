/* Working Capital */
SELECT
    ca.CompanyName,
    ca.EndPeriod,
    ca.ItemVal AS assets_current,
    cl.ItemVal AS liability_current,
    ca.ItemVal * 1.0 - cl.ItemVal AS working_capital
FROM balance_sheet ca
Join balance_sheet cl
ON ca.CompanyName = cl.CompanyName
AND ca.EndPeriod = cl.EndPeriod
WHERE ca.ItemKey = 'AssetsCurrent'
AND cl.ItemKey = 'LiabilitiesCurrent'
AND ca.CompanyName = :ticker
AND ca.EndPeriod = :end_period;