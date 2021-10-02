from etf_functions.util_function import load_website, process_table, get_attributes

FUND_NAME = "XLB"
FUND_WEBSITE = "https://www.ssga.com/us/en/individual/etfs/funds/the-materials-select-sector-spdr-fund-xlb"
TABLE_NUMBER = 21


def xlb_attributes():
    website_content = load_website(FUND_WEBSITE)
    table = process_table(website_content, table_number=TABLE_NUMBER)

    attributes = get_attributes(table)

    return attributes
