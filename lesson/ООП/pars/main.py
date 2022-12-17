from bs4 import BeautifulSoup
from datetime import date
from config import parser
import urllib.request

parser = parser("https://dzen.ru/a/Y48g5u4byCm1GdS3", "news.txt")
parser.run()