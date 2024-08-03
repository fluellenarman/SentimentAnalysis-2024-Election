import requests
from bs4 import BeautifulSoup
import urllib.parse

def getSearchUrls(query, num_pages):
    base_url = 'https://www.google.com/search'
    urls = []
    
    for start in range(0, num_pages * 10, 10):
        params = {
            'q': query,
            'tbm': 'nws',
            'start': start
        }
        search_url = f"{base_url}?{urllib.parse.urlencode(params)}"
        urls.append(search_url)
    
    return urls

def scrapeGoogleNews(query, num_pages):
    search_urls = getSearchUrls(query, num_pages)
    
    all_links = []
    for search_url in search_urls:
        print(f"Scraping {search_url}")
        response = requests.get(search_url, headers={'User-Agent': 'Mozilla/5.0'})
        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')
        links = soup.find_all('a')
        
        for link in links:
            href = link.get('href')
            if href and href.startswith('/url?q='):
                href = href.split('/url?q=')[1].split('&')[0]
                all_links.append(href)
    
    return all_links
