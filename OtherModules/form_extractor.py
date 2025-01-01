from bs4 import BeautifulSoup
import requests

class FormExtractor:
    def get_forms(self, url):
        """Extract all forms from a given URL."""
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        return soup.find_all('form')

    def extract_csrf_tokens(self, forms):
        """Find CSRF tokens in all forms and store them in a dictionary."""
        tokens = {}
        for index, form in enumerate(forms):
            form_tokens = []
            for input_tag in form.find_all('input'):
                if 'csrf' in input_tag.get('name', '').lower() or 'token' in input_tag.get('name', '').lower():
                    form_tokens.append(input_tag.get('value', ''))
            tokens[f'form_{index + 1}'] = form_tokens
        return tokens
