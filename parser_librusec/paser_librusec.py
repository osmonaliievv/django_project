import requests
from bs4 import BeautifulSoup as BS

URL = 'https://librusec.club'

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36",
}


def get_html(url, params=None):
    try:
        response = requests.get(url, headers=HEADERS, params=params)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None


def get_data(html):
    bs = BS(html, 'html.parser')
    items = bs.find_all('div', class_='item')
    books_list = []
    for item in items:
        title = item.find('div', class_='book_name')
        description = item.find('div', class_='annotation')
        img = item.find('img')
        books_list.append({
            'title': title.get_text(),
            'description': description.get_text(),
            'img': img['src'],
        })
    return books_list


def parsing():
    response = get_html(URL)
    if response and response.status_code == 200:
        books_list2 = []
        for page in range(1, 2):
            page_response = get_html(f"https://librusec.club/a/19951-evgeniy-yurevich-kleymenov", params={'page': page})
            if page_response:
                books_list2.extend(get_data(page_response.text))
        return books_list2
    else:
        raise Exception('Error in parsing')

# print(parsing())
