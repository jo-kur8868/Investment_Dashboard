CREATE TABLE IF NOT EXISTS income_stmt (
    CompanyName varchar(100) NOT NULL,
    EndPeriod varchar(100) NOT NULL,
    ItemKey varchar(100),
    ItemVal decimal
)

CREATE TABLE IF NOT EXISTS balance_sheet (
    CompanyName varchar(100) NOT NULL,
    EndPeriod varchar(100) NOT NULL,
    ItemKey varchar(100),
    ItemVal decimal
)

CREATE TABLE IF NOT EXISTS cash_flow (
    CompanyName varchar(100) NOT NULL,
    EndPeriod varchar(100) NOT NULL,
    ItemKey varchar(100),
    ItemVal decimal
)
