""" Scraping class file."""

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from bs4 import BeautifulSoup


def scroll_to_bottom(driver):
    x = 0
    old_position = 0
    new_position = None

    while new_position != old_position and x < 15:
        time.sleep(1)

        # Get old scroll position
        old_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
        # Sleep and Scroll
        time.sleep(3)
        driver.execute_script((
            "var scrollingElement = (document.scrollingElement ||"
            " document.body);scrollingElement.scrollTop ="
            " scrollingElement.scrollHeight;"))
        # Get new position
        new_position = driver.execute_script(
            ("return (window.pageYOffset !== undefined) ?"
             " window.pageYOffset : (document.documentElement ||"
             " document.body.parentNode || document.body);"))
        x += 1


class Scrap:
    def __init__(self, url) -> None:
        self.url = url

    def scrap_data(self):
        try:
            links = []
            dates = []
            times = []
            likes = []
            comments = []
            texts = []
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--window-size=1200x800")
            chrome_options.add_argument('--disable-dev-shm-usage')
            driver = webdriver.Chrome(options=chrome_options)
            driver.get(self.url)
            scroll_to_bottom(driver)
            page_source = driver.page_source
            soup = BeautifulSoup(page_source, 'lxml')
            section = soup.findAll('div', {'class': '_3drp'})
            for a in section[:100]:
                post_date_all = a.find('abbr')
                if post_date_all is None:
                    times.append('nan')
                else:
                    try:

                        post_date = post_date_all.get_text(
                            strip=True).split(',')

                        date = post_date[0]
                        time = post_date[1]
                        dates.append(date)
                        times.append(time)
                    except:

                        dates.append('today')
                        times.append(post_date_all.get_text(
                            strip=True) + ' later')
                        pass

                try:
                    x = a.find('div', attrs={
                               'class': '_52jc _5qc4 _78cz _24u0 _36xo'})
                    post_link = x.find('a')['href']
                    links.append("https://m.facebook.com/"+post_link)

                except:
                    links.append('nan')

                try:
                    like = a.find('span', attrs={'class': 'like_def _28wy'})
                    if (len(like) == 0):
                        like = 0
                    likes.append(Scrap.format_data(like.get_text(
                        strip=True).split(' ')[0]+' likes'))
                except:
                    likes.append(0)

                try:

                    text = a.find('div', {'class': '_5rgt _5nk5 _5msi'})
                    post_text = text.find('p')
                    if (len(post_text) == 0):
                        post_text = " "
                    texts.append(post_text.get_text(strip=True))
                except:
                    texts.append('nan')
                try:

                    comment = a.find('span', attrs={'class': 'cmt_def _28wy'})
                    comments.append(Scrap.format_data(comment.get_text(
                        strip=True).split(' ')[0]+' comments'))

                except:
                    comments.append(0)

                    pass

            print("link0:",links[0])
            print("link1:",links[1])
            return (links, texts, likes, comments, dates, times)
        except Exception as e:
            print(e)
            return

    @staticmethod
    def format_data(val):
        return int(val.split(' ')[0])
