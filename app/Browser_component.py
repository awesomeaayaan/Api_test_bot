from RPA.Browser.Selenium import Selenium
from RPA.Desktop import Desktop
# from RPA.Dialogs import Dialogs
# from qrlib.QRProcess import QRProcess
# from qrlib.QRComponent import QRComponent
# from Utils import remove_punctuations
import time
import logging

URL = "https://www.daraz.com.np/"
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')
SEARCH_BAR = "//input[@id='q']"
SEARCH = "//button[@class='search-box__button--1oH7']"

class DarazBot():
    def __init__(self):
        super().__init__()
        self.browser = Selenium(auto_close=True)
        self.desktop = Desktop()
        self.item_link = []

    def open_available_broser(self):
        try:
            self.browser.open_available_browser(URL)
            logging.info('open a browser')
            self.browser.maximize_browser_window()
            logging.info('maximize window')

        except:
            print("Error while opening browser")

    def get_data(self):
      pass
    def get_link(self):
        logging.info('Get Links')
        webelement = self.browser.get_webelements("//div[@class='title--wFj93']/a")
        logging.info(webelement)
        for element in webelement:
            link = self.browser.get_element_attribute(element,'href')
            logging.info(link)
            self.item_link.append(link)
        logging.info(self.item_link)


    def Scrap_item(self):
        # shadow_root = self.browser.execute_javascript("return document.querySelector('your-shadow-root-selector').shadowRoot")
        # # Switch to the Shadow DOM context
        # logging.info('Execute shadow root')
        # self.browser.switch_browser(shadow_root)
        logging.info('Scraping item')
        self.desktop.click("image:C:\\Users\\NMB\Desktop\\bot-starter-kit-v2.0\\bot-starter-kit-v2.0-optimize\\app\\image\\not_interested.png")
       
        # self.browser.wait_until_page_contains('Daz wants to be friends with you')
        # self.browser.click_button_when_visible("")
        self.browser.click_element(SEARCH_BAR)
        logging.info("click the search bar")
        self.browser.input_text(SEARCH_BAR,"pen")
        logging.info("input item in the search bar")
        self.browser.click_button(SEARCH)
        self.get_link()
        count = 0
        for links in self.item_link:
            if count < 4:
                self.browser.go_to(links)
                item_name = self.browser.get_webelement("//div[@class='pdp-product-title']/div/span").text
                logging.info(item_name)
                price = self.browser.get_webelement("//div[@class='pdp-product-price']/span").text
                logging.info(price)
                count +=1

# def main():
#     bot = DarazBot()
#     bot.open_available_broser()
#     # bot.insert_credential_and_login()


# if __name__=="__main__":
#     main()