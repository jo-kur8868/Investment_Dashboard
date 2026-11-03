CREATE TABLE IF NOT EXISTS income_statement (
    CompanyName TEXT NOT NULL,
    EndPeriod TEXT NOT NULL,
    ItemKey TEXT NOT NULL,
    ItemVal decimal,
    PRIMARY KEY (CompanyName, EndPeriod, ItemKey)
);

CREATE TABLE IF NOT EXISTS balance_sheet (
    CompanyName TEXT NOT NULL,
    EndPeriod TEXT NOT NULL,
    ItemKey TEXT NOT NULL,
    ItemVal decimal,
    PRIMARY KEY (CompanyName, EndPeriod, ItemKey)
);

CREATE TABLE IF NOT EXISTS cash_flow (
    CompanyName TEXT NOT NULL,
    EndPeriod TEXT NOT NULL,
    ItemKey TEXT NOT NULL,
    ItemVal decimal,
    PRIMARY KEY (CompanyName, EndPeriod, ItemKey)
);
