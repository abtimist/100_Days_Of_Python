import requests
from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
web_page = response.text

soup = BeautifulSoup(web_page,'html.parser')



title_tag = soup.find_all(name='h3', class_='title')

movie_titles = [movie.getText() for movie in title_tag][::-1]

with open(file="movies.txt",mode='w') as file:
    count = 0 
    for title in movie_titles:
        file.write(f"{title}\n")
 



