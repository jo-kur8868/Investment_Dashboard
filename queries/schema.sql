CREATE TABLE IF NOT EXISTS financials (
    CIK varchar(100) NOT NULL,
    CompanyName varchar(100) NOT NULL,
    EndPeriod varchar(100) NOT NULL,
    Stmt varchar(100) NOT NULL,
    Item varchar(100),
    ItemVal decimal
)
