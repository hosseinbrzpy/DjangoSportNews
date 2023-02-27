from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

n_html = requests.get('https://footba11.co/tournament/27/fixtures/%D9%86%D8%AA%D8%A7%DB%8C%D8%AC-%D9%88-%D8%A8%D8%B1'
                      '%D9%86%D8%A7%D9%85%D9%87-%D8%A8%D8%A7%D8%B2%DB%8C-%D9%87%D8%A7%DB%8C-%D9%84%DB%8C%DA%AF-%D8%A8'
                      '%D8%B1%D8%AA%D8%B1-%D8%A7%DB%8C%D8%B1%D8%A7%D9%86')
n_soup = BeautifulSoup(n_html.content, 'html.parser')
n_heading = n_soup.find_all('div', {'class': 'matches-container'})
n_news = []
for n_header in n_heading:
    n_news.append(n_header.get_text())

v_html = requests.get('http://iribf.ir/')
v_soup = BeautifulSoup(v_html.content, 'html.parser')
v_heading = v_soup.find_all('td')
v_news = []
for v_header in v_heading[0:10]:
    v_news.append(v_header.get_text())


def index(request):
    return render(request, 'index.html', {'n_news': n_news, 'v_news': v_news})
