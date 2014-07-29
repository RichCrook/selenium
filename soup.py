from bs4 import BeautifulSoup
import requests


def get_img_cnt(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content)

    return len(soup.find_all('img'))


print(get_img_cnt('http://www.imdb.com/title/tt1430612'))