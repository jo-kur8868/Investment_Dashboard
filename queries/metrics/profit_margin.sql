/* Net Profit Margin = Net Income / Sales Revenue per Sales */
SELECT
    ni.CompanyName,
    ni.EndPeriod,
    ni.ItemVal AS net_income,
    rev.ItemVal AS revenue,
    ni.ItemVal * 1.0 / NULLIF(rev.ItemVal, 0) AS net_margin
FROM income_stmt ni
JOIN income_stmt rev
ON ni.CompanyName = rev.CompanyName
AND ni.EndPeriod = rev.EndPeriod
WHERE ni.ItemKey = 'NetIncomeLoss'
AND rev.ItemKey = 'RevenueFromContractWithCustomerExcludingAssessedTax'
AND ni.CompanyName = :ticker
AND ni.EndPeriod = :end_period;