import requests
from bs4 import BeautifulSoup

URL = "https://doramy.club/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.0.0 Safari/537.36"
}


def get_html(url, params=''):
    req = requests.get(url, headers=HEADERS, params=params)
    return req


def get_data(html):
    soup = BeautifulSoup(html, "html.parser")
    items = soup.find_all('div', class_="post-home")
    # print(items)
    doramy = []
    for item in items:
        try:
            desc = item.find("table", class_="table-hom").find("tbody", class_="tbody-hom")
            doramy.append({
                "link": item.find("a").get("href"),
                "title": item.find("span").getText(),
                "authors": item.find("em").getText(),
                "series": desc.find_all("tr")[0].getText(),
                "country": desc.find_all("tr")[1].getText(),
                "year": desc.find_all("tr")[2].getText(),
                "genre": desc.find_all("tr")[3].getText(),
                "added": desc.find_all("tr")[4].getText(),
            })
        except IndexError:
            pass
    return doramy


def parser():
    html = get_html(URL)
    if html.status_code == 200:
        answer = []
        for page in range(1, 11):
            html = get_html(f"{URL}page/{page}/")
            answer.extend(get_data(html.text))
        return answer
    else:
        raise Exception("Error in parser!")