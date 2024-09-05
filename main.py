

querry = """
  WITH SALES_SUMMARY AS (
  SELECT 
      YEAR(POSTING_DATE) AS Fiscal_Year,
      CONCAT('Q', QUARTER(POSTING_DATE)) AS Fiscal_Quarter,
      LOB AS Business_Line,
      CUSTOMER_CLASSIFICATION_NAME AS Customer_Type,
      ROUND(SUM(AMT_USD_MA), 2) AS Sale_Amount_USD,
      COUNT(DISTINCT DISTRIBUTOR_NAME) AS Number_of_Distributors
  FROM
      "EDW"."CORP_REPORT"."VW_CE_DISTI_SELL_IN_BILLING"
  WHERE
      GBE_NAME = 'PSS'
      AND LOB IN ('Mobility HW', 'Print', 'Scanning HW', 'Service')
      AND AMT_USD_MA > 100
  GROUP BY
      YEAR(POSTING_DATE),
      QUARTER(POSTING_DATE),
      LOB,
      CUSTOMER_CLASSIFICATION_NAME
  )
  SELECT 
    Fiscal_Year,
    Fiscal_Quarter,
    Business_Line,
    Sale_Amount_USD,
    Number_of_Distributors,
    CASE WHEN Number_of_Distributors > 0 
         THEN ROUND(Sale_Amount_USD / Number_of_Distributors, 2)
         ELSE 0 END AS Avg_Sales_per_Distributor, -- Handle division by zero
    Customer_Type
  FROM 
    SALES_SUMMARY
  ORDER BY 
    Business_Line ASC;
"""
