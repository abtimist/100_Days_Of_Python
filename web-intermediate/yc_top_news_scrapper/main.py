from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/")

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage,'html.parser')

article_texts=[]
article_links=[]


articles = soup.find_all(name='span',class_='titleline')
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = article_tag.find('a').get('href')
    article_links.append(link)
article_points = [int(score.getText().split()[0]) for score in soup.find_all(name='span',class_='score')]



highest_upvote=article_points.index(max(article_points))

print(article_texts[highest_upvote])
print(article_links[highest_upvote])
print(article_points[highest_upvote])
