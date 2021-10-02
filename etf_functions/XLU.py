from etf_functions.util_function import load_website, process_table, get_attributes

FUND_NAME = "XLU"
FUND_WEBSITE = "https://www.ssga.com/us/en/individual/etfs/funds/the-utilities-select-sector-spdr-fund-xlu"
TABLE_NUMBER = 21


def xlu_attributes():
    website_content = load_website(FUND_WEBSITE)
    table = process_table(website_content, table_number=TABLE_NUMBER)

    attributes = get_attributes(table)

    return attributes
