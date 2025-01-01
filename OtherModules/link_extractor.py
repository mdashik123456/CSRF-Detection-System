import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, urljoin


class LinkExtractor:
    """A class to extract all valid links from a given URL."""
    
    def __init__(self, url):
        self.url = url
        self.links = []

    def fetch_html(self):
        """Fetches the HTML content of the given URL."""
        try:
            response = requests.get(self.url)
            response.raise_for_status()  # Raise an exception for HTTP errors
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error fetching URL: {e}")
            return None

    def is_valid_link(self, link):
        """
        Checks if a link is valid.
        A valid link:
        - Has a scheme (e.g., http, https)
        - Does not contain 'javascript:void(0)' or similar invalid patterns
        """
        parsed = urlparse(link)
        return bool(parsed.netloc) and bool(parsed.scheme)

    def extract_links(self, html_content):
        """Extracts and validates all links from the HTML content."""
        soup = BeautifulSoup(html_content, 'html.parser')
        for link_tag in soup.find_all('a', href=True):
            href = link_tag['href']
            # Convert relative URLs to absolute URLs
            full_url = urljoin(self.url, href)
            if self.is_valid_link(full_url):
                self.links.append(full_url)

    def get_links(self):
        """Main method to get all valid links from the webpage."""
        html_content = self.fetch_html()
        if html_content:
            self.extract_links(html_content)
        return self.links
