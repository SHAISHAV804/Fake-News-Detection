import csv
import requests
from bs4 import BeautifulSoup

def getNewsData():
    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"
    }
    response = requests.get(
        "https://www.google.com/search?q=election+2024+india&num=100&sca_esv=e7f9f9d91f1faf1c&gl=us&tbm=nws&ei=XZMqZqSBMragnesPzN2wgA4&oq=election+2024&gs_lp=Egxnd3Mtd2l6LW5ld3MiDWVsZWN0aW9uIDIwMjQqAggEMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATILEAAYgAQYsQMYgwEyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDATIOEAAYgAQYsQMYgwEYigUyCxAAGIAEGLEDGIMBMgsQABiABBixAxiDAUjX8QFQq6MBWKfaAXACeACQAQCYAZQCoAGuEqoBBjAuMTUuMbgBAcgBAPgBAZgCEqAC6hLCAgoQABiABBhDGIoFwgIFEAAYgATCAgcQABiABBgKwgILEAAYgAQYkQIYigXCAggQABiABBixA8ICDhAAGIAEGJECGLEDGIoFwgIQEAAYgAQYsQMYQxiDARiKBcICERAAGIAEGJECGLEDGIMBGIoFwgIGEAAYFhgewgIIEAAYFhgeGA_CAgQQABgDmAMAiAYBkgcGMi4xNS4xoAeOXA&sclient=gws-wiz-news", headers=headers
    )
    soup = BeautifulSoup(response.content, "html.parser")
    news_results = []
 
    for el in soup.select("div.SoaBEf"):
        link = el.find("a")["href"]
        title = el.select_one("div.MBeuO").get_text()
        date = el.select_one(".LfVVr").get_text()
        source = el.select_one(".NUnG9d span").get_text()
        
        # Fetching the full news description from the article link
        article_response = requests.get(link, headers=headers)
        article_soup = BeautifulSoup(article_response.content, "html.parser")
        snippet = article_soup.find("meta", attrs={"name": "description"})["content"]
        
        news_results.append({
            "link": link,
            "title": title,
            "snippet": snippet,
            "date": date,
            "source": source
        })

    return news_results

news_data = getNewsData()

with open("news_data.csv", "w", newline="", encoding="utf-8") as csv_file:
    fieldnames = ["link", "title", "snippet", "date", "source"]
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(news_data)

print("Data saved to news_data.csv")
