from edgar import set_identity, Company

# Enter your name and your email address
set_identity()

class Fetcher():
    def __init__(self, _ticker):
        self.ticker = _ticker

    def get_Ticker(self):
            return self.ticker

    def set_Ticker(self, name):
        self.ticker = name

    def get_income_stmt(self):
        company = Company(self.get_Ticker())
        income_stmt = company.get_financials().income_statement()
        df = income_stmt.to_dataframe()

        return df.iloc[0].to_dict()
    


