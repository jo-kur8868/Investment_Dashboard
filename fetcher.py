from edgar import set_identity, Company
import pandas as pd

set_identity("")

company = Company("AAPL")
income_stmt = company.get_financials().income_statement()
df = income_stmt.to_dataframe()

row_dict = df.iloc[0].to_dict()
print(row_dict['concept'])

