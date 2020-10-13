import requests
from bs4 import BeautifulSoup
import pprint


res = requests.get('https://news.ycombinator.com/news')
res2 = requests.get('https://news.ycombinator.com/news?p=2')
soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')
links = soup.select('.storylink')
links2 = soup2.select('.storylink')
subtext = soup.select('.subtext')
subtext2 = soup2.select('.subtext')

combined_links = links + links2
combined_subtext = subtext + subtext2

def sort_by_votes(hn_list):
    return sorted(hn_list, key=lambda k:k['points'], reverse=True)

def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({'Title': title, 'Link': href, 'points': points})
    return sort_by_votes(hn)

pprint.pprint(create_custom_hn(combined_links, combined_subtext))