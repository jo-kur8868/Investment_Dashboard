from edgar import set_identity, Company

# Enter your name and your email address
set_identity( )

income = Company('AAPL').income_statement().to_dataframe()
income = income.loc[income['is_abstract'] == False]

# For FY 2025
for key, val in income['FY 2025'].items():
    print(key, val)
