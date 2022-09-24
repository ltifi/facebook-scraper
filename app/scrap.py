""" Scraping class file."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class Scrap:
    def __init__(self, url) -> None:
        self.url = url

    def scrap_data(self):
        try:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--window-size=1200x800")
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            title_page = driver.find_element_by_xpath(
                ".//div[@class= 'mfn553m3 th51lws0']").text
            elm = driver.find_elements_by_xpath(
                ".//div[@class= 'pytsy3co cqf1kptm alzwoclg']/div")
            li = [e.text for e in elm]
            print(li)
            # nb_likes = int(li[3].split()[0].replace(',', ''))
            # nb_followers = int(li[4].split()[0].replace(',', ''))
            nb_likes = Scrap.format_data(li[3].split()[0])
            nb_followers = Scrap.format_data(li[4].split()[0])
            location = li[0]
            website = li[6]
            email = li[7]
            categorie = li[9].split()[0]
            return (title_page, nb_likes, nb_followers, location, website, email, categorie)
        except Exception as e:
            print(e)
            return

    @staticmethod
    def format_data(val):
        return int(val.replace(',', ''))
