/* Net Profit Margin = Net Income / Sales Revenue per Sales */
SELECT
    ni.CompanyName,
    ni.EndPeriod,
    ni.ItemVal AS net_income,
    rev.ItemVal AS revenue,
    ni.ItemVal * 100.0 / NULLIF(rev.ItemVal, 0) AS net_margin
FROM income_statement ni
JOIN income_statement rev
ON ni.CompanyName = rev.CompanyName
AND ni.EndPeriod = rev.EndPeriod
WHERE ni.ItemKey = 'NetIncomeLoss'
AND rev.ItemKey = 'RevenueFromContractWithCustomerExcludingAssessedTax'
AND ni.CompanyName = :ticker
AND ni.EndPeriod = :end_period;