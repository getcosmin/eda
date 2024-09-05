

querry = """
  SELECT 
    YEAR(POSTING_DATE) AS "Fiscal Year",
    CONCAT('Q', QUARTER(POSTING_DATE)) AS "Fiscal Quarter",
    LOB AS "Business Line"
    ROUND(SUM(AMT_USD_MA)) AS "Sale Amount USD",
    COUNT(DISTINCT DISTRIBUTOR_NAME) AS "Number of Distributors",
    ROUND("Sale Amount USD" / "Number of Distributors") AS "Avg. Sales per Distributors"),
    CUSTOMER_CLASSIFICATION_NAME AS "Customer Type"
  FROM
    "EDW"."CORP_REPORT"."VW_CE_DISTI_SELL_IN_BILLING"
  WHERE
    GBE_NAME = 'PSS'
    AND "Business Line" IN ('Mobility HW', 'Print', 'Scanning HW', 'Service')
    AND AMT_USD_MA > 100
  GROUP BY
    "Fiscal Year",
    "Fiscal Quarter",
    "Business Line",
    "Customer Type"
  ORDER BY
    "Business Line" ASC  
"""
