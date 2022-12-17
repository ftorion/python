from bs4 import BeautifulSoup
from datetime import date
import urllib.request

ur = "https://dzen.ru/a/Y48g5u4byCm1GdS3"
reg = urllib.request.urlopen(ur)
html = reg.read()
soup = BeautifulSoup(html, "html.parser")
news = soup.find_all("p", class_="article-render__block article-render__block_unstyled")
f = open("pars.txt", "w", encoding="utf-8")
for item in news:
    title = item.find("span").get_text(strip=True)
    f.write(title + "\n")
else:
    f.write(f"Дата парсинга с сайта {date.today()}, {ur}")
f.close()
