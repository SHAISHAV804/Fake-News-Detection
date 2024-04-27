
from bs4 import BeautifulSoup
import pandas as pd
import requests
data = pd.read_csv('news_data.csv', encoding ='latin-1')


def scrape_website_text(url):

    try:
        # Send a GET request to the URL
        response = requests.get(url)

        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')

        # Extract the text content within the <p> tags
        p_tags = soup.find_all('p')
        text_content = '\n'.join([p.get_text() for p in p_tags])

        word_count = len(text_content.split())
        if word_count > 750:
            text_content = ' '.join(text_content.split()[:750]) + '...'

        return text_content

    except requests.exceptions.RequestException as e:
        print(f"Error scraping website: {e}")
        return None


# Add a new 'description' column to the DataFrame
data['description'] = ''

for index, row in data.iterrows():
    url = row['link']
    text_content = scrape_website_text(url)
    if text_content:
        data.at[index, 'description'] = text_content

# Save the updated DataFrame to a new CSV file
data.to_csv('new_with_desription.csv', index=False)