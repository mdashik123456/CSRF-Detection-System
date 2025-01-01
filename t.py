import requests
from bs4 import BeautifulSoup

def extract_links(url):
    try:
        # Fetch the webpage content
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors

        # Parse HTML content
        soup = BeautifulSoup(response.text, 'html.parser')
        links = []

        # Extract all <a> tags with href attributes
        for link in soup.find_all('a', href=True):
            links.append(link['href'])

        return links

    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return []

# Example usage
url = "https://yts.mx/"
all_links = extract_links(url)
print("Extracted Links:")
for link in all_links:
    print(link)