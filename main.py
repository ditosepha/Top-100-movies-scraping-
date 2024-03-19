import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


respons = requests.get(url=URL)

empire_web_page = respons.text

soup = BeautifulSoup(empire_web_page, "html.parser")

h3_elem = soup.find_all(name="h3", class_="title")

titles = [h3.text for h3 in h3_elem]
titles.reverse()



with open("movies.txt", "w", encoding="utf-8") as file:
    for movies in titles:
        file.write(f"{movies}\n")
        

