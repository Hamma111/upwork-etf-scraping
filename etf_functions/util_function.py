import requests
from bs4 import BeautifulSoup
import pandas as pd
from SETTINGS import NAV_ATTR_NAME, SO_ATTR_NAME, AUM_ATTR_NAME


def load_website(fund_website):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/89.0.4389.90 Safari/537.36 Edg/89.0.774.63',
    }
    site = requests.get(fund_website, headers=headers)
    soup = BeautifulSoup(site.content, 'html.parser')
    print(soup.title.text, fund_website)
    return site.text


def process_table(website_content, table_number):
    """
    This function does sth
    :param website_content:
    :param table_number:
    :return:
    """
    df = pd.read_html(website_content)[table_number]
    df.iloc[0, 0] = NAV_ATTR_NAME
    df.iloc[1, 0] = SO_ATTR_NAME
    df.iloc[2, 0] = AUM_ATTR_NAME
    return df.copy()


def get_attributes(table):
    df = table.copy()
    nav_attr = df[df.iloc[:, 0] == NAV_ATTR_NAME].iloc[0, 1]
    so_attr = df[df.iloc[:, 0] == SO_ATTR_NAME].iloc[0, 1]
    aum_attr = df[df.iloc[:, 0] == AUM_ATTR_NAME].iloc[0, 1]

    serialized_attributes_list = [nav_attr, so_attr, aum_attr]

    return serialized_attributes_list
