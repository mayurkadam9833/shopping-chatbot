import requests
from bs4 import BeautifulSoup
import time

headers = {"User-Agent": "Mozilla/5.0"}
categories = ["laptops", "mobiles", "headphones"]
product_links = []

for category in categories:
    print(f"Fetching category: {category}")
    for page in range(1, 6):  # scrape first 5 pages per category
        url = f"https://www.flipkart.com/search?q={category}&page={page}"
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        
        for a in soup.find_all("a", href=True):
            if "/p/" in a['href']:
                full_url = "https://www.flipkart.com" + a['href']
                if full_url not in product_links:
                    product_links.append(full_url)
        
        print(f"  Page {page} → {len(product_links)} total links")
        time.sleep(1)  # polite delay to avoid getting blocked

print(f"\n✅ Total product URLs collected: {len(product_links)}")