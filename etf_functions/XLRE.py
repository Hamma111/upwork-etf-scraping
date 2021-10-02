from etf_functions.util_function import load_website, process_table, get_attributes

FUND_NAME = "XLRE"
FUND_WEBSITE = "https://www.ssga.com/us/en/individual/etfs/funds/the-real-estate-select-sector-spdr-fund-xlre"
TABLE_NUMBER = 21


def xlre_attributes():
    website_content = load_website(FUND_WEBSITE)
    table = process_table(website_content, table_number=TABLE_NUMBER)

    attributes = get_attributes(table)

    return attributes
