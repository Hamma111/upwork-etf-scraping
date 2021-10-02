import pyautogui as auto
from random import randint, random
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def getChromeInstance(headless=False):
    """Returns some fancy options for selenium webdrive which makes the browser look like a real browser and not
    some bot."""
    options = Options()
    if headless:
        options.add_argument('headless')
    #     options.add_argument('--no-sandbox')
    #     options.add_argument('--disable-dev-shm-usage')
    options.add_argument("--disable-blink-features")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    driver = webdriver.Chrome(options=options)
    return driver


num_minutes = 20
num_seconds = 20 * 60

sites = ['https://www.ssga.com/us/en/individual/etfs/funds/the-materials-select-sector-spdr-fund-xlb',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-communication-services-select-sector-spdr-fund-xlc',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-energy-select-sector-spdr-fund-xle',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-financial-select-sector-spdr-fund-xlf',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-industrial-select-sector-spdr-fund-xli',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-technology-select-sector-spdr-fund-xlk',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-consumer-staples-select-sector-spdr-fund-xlp',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-real-estate-select-sector-spdr-fund-xlre',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-utilities-select-sector-spdr-fund-xlu',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-health-care-select-sector-spdr-fund-xlv',
         'https://www.ssga.com/us/en/individual/etfs/funds/the-consumer-discretionary-select-sector-spdr-fund-xly']

dr = getChromeInstance()
dr.get(sites[randint(1, 10)])
sleep(10)

for i in range(num_seconds):
    if i % 50 == 0:
        dr.get(sites[randint(1, 10)])

    if i % 10 == 0:
        for _ in range(randint(1, 5)):
            dr.find_element_by_tag_name("body").send_keys(Keys.PAGE_UP)

        for _ in range(randint(1, 5)):
            dr.find_element_by_tag_name("body").send_keys(Keys.PAGE_DOWN)

    # if i % 10 == 0:
    #     choice = randint(1, 4)
    #     if choice == 1:
    #         auto.hotkey('win', 'up')
    #     if choice == 2:
    #         auto.hotkey('win', 'up')
    #     if choice == 3:
    #         auto.hotkey('win', 'left')
    #     if choice == 4:
    #         auto.hotkey('win', 'right')
    #     auto.hotkey('space')

    if i % 5 == 0:
        choice = randint(1, 2)
        if choice == 1:
            auto.hotkey('alt', 'tab')
        if choice == 2:
            auto.hotkey('ctrl', 'tab')

    try:
        auto.moveTo(randint(1, 200), randint(1, 200), 0.25)
        auto.keyDown('scrolllock')
        auto.keyUp('scrolllock')
        auto.hotkey('a')
        auto.hotkey('backspace')

    except auto.FailSafeException as ex:
        print("caught")

    sleep(random())
