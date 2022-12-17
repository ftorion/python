from bs4 import BeautifulSoup
import urllib.request
class parser:
    html = ""
    soup = ""
    lis = []

    def __init__(self, url, file):
        self.url = url
        self.file = file

    def pars(self):
        news = self.soup.find_all("p", class_="article-render__block article-render__block_unstyled")
        for item in news:
            title = item.find("span").get_text(strip=True)
            self.save(title.text)
    def get_html(self):
        reg = urllib.request.urlopen(self.url)
        self.html = reg.read()
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.pars()
    def save(self, text):
        with open(self.file, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    def run(self):
        self.get_html()
