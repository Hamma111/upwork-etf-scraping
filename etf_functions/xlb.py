import requests
from bs4 import BeautifulSoup
import pandas as pd
from .util_function import load_website


FUND_NAME = "XLB"
FUND_WEBSITE = "https://www.ssga.com/us/en/individual/etfs/funds/the-materials-select-sector-spdr-fund-xlb"


#
# def load_website():
#     headers = {
#         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                       'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63',
#     }
#     site = requests.get(FUND_WEBSITE, headers=headers)
#     return site.text


def process_tables(website_content):
    df = pd.read_html(website_content)[21]



def xlb_attributes():

    return
